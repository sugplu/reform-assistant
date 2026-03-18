def load_knowledge_files() -> list[dict]:
    docs = []
    if not KNOWLEDGE_DIR.exists():
        return docs

    for file_path in sorted(KNOWLEDGE_DIR.iterdir()):
        if file_path.suffix.lower() not in {".txt", ".md"}:
            continue
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
            docs.append({"name": file_path.name, "text": text})
            logger.info("Loaded knowledge file: %s (%s chars)", file_path.name, len(text))
        except Exception as exc:
            logger.warning("Could not read %s: %s", file_path.name, exc)
    return docs


KNOWLEDGE_DOCS = load_knowledge_files()
