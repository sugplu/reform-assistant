import json
import logging
import os
import threading
import time
from html.parser import HTMLParser
from pathlib import Path
from typing import List

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

app = FastAPI(title="Reform California Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ---------------------------------------------------------------------------
# Knowledge loading and retrieval
# ---------------------------------------------------------------------------
def load_knowledge_files() -> list[dict]:
    docs = []
    if not KNOWLEDGE_DIR.exists():
        logger.warning("knowledge directory not found at %s", KNOWLEDGE_DIR)
        return docs

    for file_path in sorted(KNOWLEDGE_DIR.iterdir()):
        if file_path.suffix.lower() not in {".txt", ".md"}:
            continue

        try:
            text = file_path.read_text(encoding="utf-8", errors="replace").strip()
            if text:
                docs.append({"name": file_path.name, "text": text})
                logger.info("Loaded knowledge file: %s (%s chars)", file_path.name, len(text))
        except Exception as exc:
            logger.warning("Could not read %s: %s", file_path.name, exc)

    return docs


def chunk_text(text: str, chunk_size: int = 2200, overlap: int = 250) -> list[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= text_length:
            break
        start += chunk_size - overlap

    return chunks


def build_knowledge_chunks(docs: list[dict]) -> list[dict]:
    chunks = []

    for doc in docs:
        for idx, chunk in enumerate(chunk_text(doc["text"])):
            chunks.append(
                {
                    "source": doc["name"],
                    "chunk_id": idx,
                    "text": chunk,
                    "search_text": chunk.lower(),
                }
            )

    logger.info("Built %s knowledge chunks", len(chunks))
    return chunks


KNOWLEDGE_DOCS = load_knowledge_files()
KNOWLEDGE_CHUNKS = build_knowledge_chunks(KNOWLEDGE_DOCS)


def get_relevant_knowledge(query: str, max_chunks: int = 5, max_chars: int = 10000) -> str:
    if not query.strip() or not KNOWLEDGE_CHUNKS:
        return ""

    terms = [term.lower() for term in query.split() if len(term.strip()) > 2]
    if not terms:
        return ""

    scored = []
    for item in KNOWLEDGE_CHUNKS:
        score = 0
        for term in terms:
            score += item["search_text"].count(term)

        if score > 0:
            scored.append((score, item))

    scored.sort(key=lambda row: row[0], reverse=True)

    selected = []
    total_chars = 0
    seen = set()

    for score, item in scored:
        key = (item["source"], item["chunk_id"])
        if key in seen:
            continue

        formatted = f"=== SOURCE: {item['source']} ===\n{item['text']}"
        if total_chars + len(formatted) > max_chars:
            break

        selected.append(formatted)
        seen.add(key)
        total_chars += len(formatted)

        if len(selected) >= max_chunks:
            break

    return "\n\n".join(selected)


# ---------------------------------------------------------------------------
# Live site fetcher
# ---------------------------------------------------------------------------
class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []
        self.skip_depth = 0
        self.skip_tags = {"script", "style", "nav", "footer", "head", "header"}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.skip_depth > 0:
            self.skip_depth -= 1

    def handle_data(self, data):
        if self.skip_depth == 0:
            cleaned = " ".join(data.split())
            if cleaned:
                self.parts.append(cleaned)

    def get_text(self) -> str:
        return " ".join(self.parts)


def fetch_page(url: str, max_chars: int = 2200) -> str:
    try:
        response = httpx.get(
            url,
            timeout=15,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 ReformCA-Assistant/1.0"},
        )
        response.raise_for_status()
        parser = TextExtractor()
        parser.feed(response.text)
        return parser.get_text()[:max_chars]
    except Exception as exc:
        logger.warning("Could not fetch %s: %s", url, exc)
        return ""


LIVE_PAGES = [
    ("Home", "https://reformcalifornia.org/"),
    ("Events", "https://reformcalifornia.org/events"),
    ("Campaigns", "https://reformcalifornia.org/campaigns"),
    ("Volunteer", "https://reformcalifornia.org/volunteer"),
    ("Voter Guides", "https://reformcalifornia.org/voter-guides"),
]

live_context = {
    "content": "",
    "last_updated": 0.0,
}


def refresh_live_context() -> None:
    logger.info("Refreshing live site content...")
    parts = []

    for label, url in LIVE_PAGES:
        text = fetch_page(url)
        if text:
            parts.append(f"[{label} - {url}]\n{text}")

    live_context["content"] = "\n\n".join(parts)
    live_context["last_updated"] = time.time()
    logger.info("Live content refreshed.")


def background_refresh(interval_seconds: int = 3600) -> None:
    while True:
        time.sleep(interval_seconds)
        refresh_live_context()


refresh_live_context()
threading.Thread(target=background_refresh, daemon=True).start()


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------
BASE_SYSTEM_PROMPT = """
You are the official 24/7 public assistant for Reform California and Chairman Carl DeMaio.
Your role is to help supporters, voters, donors, and the public get accurate information
and take immediate action. You are knowledgeable, warm, professional, and action-oriented.
You speak on behalf of Reform California's team. You are not Carl himself.

RESPONSE RULES
1. Give the direct answer first.
2. Add the best link or contact.
3. Offer a clear next step or action.
4. Use numbered steps for multi-step processes.
5. Keep answers concise but complete.
6. Never invent facts, dates, endorsements, office details, petition details, or deadlines.
7. If a detail is uncertain or not verified, say so clearly and direct the user to the official source.

SOURCE PRIORITY
1. Official Reform California website and official public pages.
2. Relevant snippets from uploaded knowledge files.
3. Live fetched website content included in this prompt.
4. General public facts only when necessary and low risk.

ORGANIZATION OVERVIEW
Reform California is a grassroots political organization focused on:
- Taxpayer protection
- Public safety improvement
- Education reform and parental rights
- Election integrity

Three core priorities:
- Make California Affordable Again
- Make California Safe Again
- Make California Dream Again

KEY LINKS
Main website: https://reformcalifornia.org
Events / Town Halls: https://reformcalifornia.org/events
Volunteer signup: https://reformcalifornia.org/volunteer
Volunteer activities: https://reformcalifornia.org/volunteer-activities
Volunteer shifts: https://reformcalifornia.volunteershift.com/shifts?sort=soonest
All campaigns: https://reformcalifornia.org/campaigns
Election Integrity: https://reformcalifornia.org/campaigns/election-integrity-initiative
Block Rate Hikes: https://reformcalifornia.org/campaigns/block-the-rate-hikes
Voter guides: https://reformcalifornia.org/voter-guides
Statewide guide: https://reformcalifornia.org/voter-guides/california
Petition mail form: https://reformcalifornia.org/forms/volunteer-to-stop-the-savings-tax
Signature volunteer form: https://reformcalifornia.org/forms/election-integrity-signature-volunteer-sign-up
Voter registration: https://www.sos.ca.gov/elections/registration-status
Polling place lookup: https://www.sos.ca.gov/elections/polling-place
Ballot tracking: https://www.trackmyballot.org
Campaign finance: https://cal-access.sos.ca.gov/

CONTACT
Volunteer hotline: 619-354-7257
Volunteer email: volunteers@reformcalifornia.org
Walk-in office: 1320 W Valley Pkwy #304, Escondido CA 92029
Mailing address: Reform California, PO Box 27227, San Diego, CA 92198

PETITION RULES
- Always distinguish between an online interest form and an official ballot petition.
- Online form means interest/request only. It is not an official signature.
- Official ballot petitions require a physical wet signature.
- Do not claim petitions can be completed online unless the official site explicitly says so.
- Do not invent downloadable petition options.

ENDORSEMENTS
- Only reference officially published endorsements.
- Never speculate about endorsements.

EVENTS
- Do not invent event dates, venues, or schedules.
- Use official event pages or clearly say when the user should check the events page.

VOTER GUIDES
- If a race or candidate is missing, do not speculate.
- Say Reform California either did not endorse or did not publish guidance.

DONATIONS
- Direct donors to the official website.
- Do not provide tax or legal advice.

GUARDRAILS
- Never provide confidential, internal, or staff-only information.
- Do not speculate.
- Do not argue with users.
- No legal, tax, or campaign finance advice.
- If asked about something not verified, direct the user to the official source.

TONE
Professional, warm, clear, plain-language, and action-oriented.
Express appreciation when users want to volunteer, donate, or help.
""".strip()


def build_system_prompt(user_query: str) -> str:
    prompt = BASE_SYSTEM_PROMPT

    relevant_knowledge = get_relevant_knowledge(user_query)
    if relevant_knowledge:
        prompt += (
            "\n\n━━━ RELEVANT KNOWLEDGE SNIPPETS ━━━\n"
            "Use these snippets when relevant. Do not assume anything beyond them.\n\n"
            f"{relevant_knowledge}"
        )

    if live_context["content"]:
        age_minutes = int((time.time() - live_context["last_updated"]) / 60)
        prompt += (
            f"\n\n━━━ LIVE SITE CONTENT (refreshed {age_minutes} min ago) ━━━\n"
            "Use this for current website content, events, campaigns, and updates.\n\n"
            f"{live_context['content'][:7000]}"
        )

    return prompt


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


def normalize_messages(messages: List[Message]) -> List[dict]:
    allowed_roles = {"user", "assistant"}
    normalized = []

    for message in messages:
        role = message.role if message.role in allowed_roles else "user"
        normalized.append({"role": role, "content": message.content})

    return normalized


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
async def root():
    index_path = STATIC_DIR / "index.html"
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.get("/health")
async def health():
    age_minutes = int((time.time() - live_context["last_updated"]) / 60) if live_context["last_updated"] else None
    return {
        "status": "ok",
        "knowledge_files_loaded": len(KNOWLEDGE_DOCS),
        "knowledge_chunks_loaded": len(KNOWLEDGE_CHUNKS),
        "live_content_loaded": bool(live_context["content"]),
        "live_content_age_mins": age_minutes,
    }


@app.post("/chat")
async def chat(body: ChatRequest):
    messages = normalize_messages(body.messages)
    latest_user_message = next((m.content for m in reversed(body.messages) if m.role == "user"), "")
    system_prompt = build_system_prompt(latest_user_message)

    def generate():
        try:
            stream = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o"),
                messages=[{"role": "system", "content": system_prompt}] + messages,
                stream=True,
                max_completion_tokens=int(os.getenv("MAX_TOKENS", "700")),
                temperature=float(os.getenv("TEMPERATURE", "0.2")),
            )

            for chunk in stream:
                delta = chunk.choices[0].delta
                if getattr(delta, "content", None):
                    yield f"data: {json.dumps({'content': delta.content})}\n\n"

            yield "data: [DONE]\n\n"
        except Exception as exc:
            logger.error("OpenAI error: %s", exc)
            yield f"data: {json.dumps({'error': 'Something went wrong. Please try again or call 619-354-7257.'})}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
