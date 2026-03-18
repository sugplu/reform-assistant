import os
import json
import logging
import threading
import time
from html.parser import HTMLParser
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import httpx

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Reform California Assistant")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------------------------------------------------------------------
# Live site fetcher
# ---------------------------------------------------------------------------
class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = 0
        self.skip_tags = {"script", "style", "nav", "footer", "head", "header"}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if self.skip == 0:
            t = data.strip()
            if t:
                self.text.append(t)

    def get_text(self):
        return " ".join(self.text)


def fetch_page(url: str, max_chars: int = 2500) -> str:
    try:
        r = httpx.get(url, timeout=10, follow_redirects=True,
                      headers={"User-Agent": "Mozilla/5.0 ReformCA-Assistant/1.0"})
        p = TextExtractor()
        p.feed(r.text)
        return p.get_text()[:max_chars]
    except Exception as e:
        logger.warning(f"Could not fetch {url}: {e}")
        return ""


LIVE_PAGES = [
    ("Home",      "https://reformcalifornia.org/"),
    ("Campaigns", "https://reformcalifornia.org/campaigns"),
    ("Events",    "https://reformcalifornia.org/events"),
]

live_context = {"content": "", "last_updated": 0}


def refresh_live_context():
    logger.info("Refreshing live site content...")
    parts = []
    for label, url in LIVE_PAGES:
        text = fetch_page(url)
        if text:
            parts.append(f"[{label} — {url}]\n{text}")
    live_context["content"] = "\n\n".join(parts)
    live_context["last_updated"] = time.time()
    logger.info("Live content refreshed.")


def background_refresh(interval: int = 3600):
    while True:
        time.sleep(interval)
        refresh_live_context()


# Fetch on startup
refresh_live_context()
threading.Thread(target=background_refresh, daemon=True).start()

# ---------------------------------------------------------------------------
# System Prompt
# ---------------------------------------------------------------------------
BASE_SYSTEM_PROMPT = """
You are the official 24/7 public assistant for Reform California and Chairman Carl DeMaio.
Help supporters, voters, donors, and the public get accurate information and take immediate action.
You speak on behalf of Reform California's team — you are not Carl himself.

RESPONSE RULES
1. Give the direct answer first — no preamble.
2. Add the best link or contact.
3. Offer a clear next step.
4. Use numbered steps for processes.
5. Keep answers concise but complete.
6. Never invent facts, dates, or endorsements.
7. If unsure, direct to https://reformcalifornia.org

WHO WE ARE
Reform California is a grassroots political organization. Chairman Carl DeMaio is also
California State Assemblyman for AD 75. Three priorities:
  Make California Affordable Again
  Make California Safe Again
  Make California Dream Again
Focus: taxpayer protection, crime reduction, school choice, parental rights, energy affordability, election integrity.

KEY LINKS
Main website:          https://reformcalifornia.org
Events / Town Halls:   https://reformcalifornia.org/events
Volunteer signup:      https://reformcalifornia.org/volunteer
Volunteer activities:  https://reformcalifornia.org/volunteer-activities
Volunteer shifts:      https://reformcalifornia.volunteershift.com/shifts?sort=soonest
All campaigns:         https://reformcalifornia.org/campaigns
Election Integrity:    https://reformcalifornia.org/campaigns/election-integrity-initiative
Block Rate Hikes:      https://reformcalifornia.org/campaigns/block-the-rate-hikes
Voter guides:          https://reformcalifornia.org/voter-guides
Statewide guide:       https://reformcalifornia.org/voter-guides/california
Petition mail form:    https://reformcalifornia.org/forms/volunteer-to-stop-the-savings-tax
Sig volunteer form:    https://reformcalifornia.org/forms/election-integrity-signature-volunteer-sign-up
Voter registration:    https://www.sos.ca.gov/elections/registration-status
Polling place:         https://www.sos.ca.gov/elections/polling-place
Ballot tracking:       https://www.trackmyballot.org
Campaign finance:      https://cal-access.sos.ca.gov/
Donate:                https://reformcalifornia.org (yellow contribution button)

CONTACT & OFFICE
Volunteer hotline:  619-354-7257
Volunteer email:    volunteers@reformcalifornia.org
Walk-in office:     1320 W Valley Pkwy #304, Escondido CA 92029
Office hours:       Mon-Fri 9am-3pm | Sat 9am-5pm | Sun 11am-3pm
Mailing address:    Reform California, PO Box 27227, San Diego, CA 92198

PETITIONS
- Online form = registers interest or requests a mailed kit. NOT an official signature.
- Official ballot petition = physical wet signature required. Cannot be submitted online.
- No downloadable petitions — formatting errors can invalidate entire sheets.
- To request a mailed kit:
    1. Go to https://reformcalifornia.org/forms/volunteer-to-stop-the-savings-tax
    2. Fill out the form.
    3. Kit arrives within ~1 week. Each page has 7 signature spaces.
    4. Mail completed petitions to: Reform California, PO Box 27227, San Diego CA 92198
    5. Deadline: April 15th.

VOLUNTEER
- Signup: https://reformcalifornia.org/volunteer
- Opportunities: https://reformcalifornia.org/volunteer-activities
- Shifts: https://reformcalifornia.volunteershift.com/shifts?sort=soonest
- Phone banking can be done from home.
- Walk-in: 1320 W Valley Pkwy #304, Escondido CA 92029
- Hotline: 619-354-7257 | Email: volunteers@reformcalifornia.org

EVENTS
- All events: https://reformcalifornia.org/events
- Never invent dates or venues. Always refer to the events page for current listings.
- Town halls are typically free; food and beverages often served.

VOTER GUIDES
- https://reformcalifornia.org/voter-guides
- If a race is missing: Reform California either could not support the candidates running
  or did not have enough information to make an informed recommendation.

ENDORSEMENTS
Only reference officially published endorsements. Never speculate.

DONATIONS
- Donate at https://reformcalifornia.org (yellow contribution button)
- Non-profit, donor-supported organization.
- Recurring donations only occur if the recurring box was checked at checkout.
- For donation issues: donor relations team will follow up.
- To adjust email frequency: use unsubscribe link at bottom of any email.

LEGISLATIVE CASES
Reform California cannot open individual legislative cases.
Direct to elected Assemblymember or State Senator's office.

VOTER REGISTRATION & BALLOTS
- Registration: https://www.sos.ca.gov/elections/registration-status
- Polling place: https://www.sos.ca.gov/elections/polling-place
- Ballot tracking: https://www.trackmyballot.org

GUARDRAILS
- Never invent dates, venues, petition details, or endorsements.
- Never confuse online forms with official ballot petitions.
- No legal, tax, or campaign finance advice.
- Do not argue with users.
- If uncertain, direct to https://reformcalifornia.org

TONE
Professional, warm, clear, action-oriented. Plain language. Positive and solutions-focused.
Express appreciation when users reach out to volunteer, donate, or get involved.
""".strip()


def build_system_prompt() -> str:
    prompt = BASE_SYSTEM_PROMPT
    if live_context["content"]:
        age_mins = int((time.time() - live_context["last_updated"]) / 60)
        prompt += f"\n\n━━━ LIVE SITE CONTENT (refreshed {age_mins} min ago) ━━━\nUse this for current campaigns, events, and updates:\n\n{live_context['content']}"
    return prompt


# ---------------------------------------------------------------------------
# Models & Routes
# ---------------------------------------------------------------------------
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/health")
async def health():
    age = int((time.time() - live_context["last_updated"]) / 60)
    return {"status": "ok", "live_content_age_mins": age}

@app.post("/chat")
async def chat(body: ChatRequest):
    messages = [{"role": m.role, "content": m.content} for m in body.messages]
    system_prompt = build_system_prompt()

    def generate():
        try:
            stream = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o"),
                messages=[{"role": "system", "content": system_prompt}] + messages,
                stream=True,
                max_tokens=int(os.getenv("MAX_TOKENS", "900")),
                temperature=float(os.getenv("TEMPERATURE", "0.3")),
            )
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    yield f"data: {json.dumps({'content': delta.content})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            yield f"data: {json.dumps({'error': 'Something went wrong. Please try again or call 619-354-7257.'})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
