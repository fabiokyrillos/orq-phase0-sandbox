import re
import unicodedata


def slugify(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    without_accents = "".join(c for c in decomposed if not unicodedata.combining(c))
    lowered = without_accents.lower()
    hyphenated = re.sub(r"[^a-z0-9]+", "-", lowered)
    return hyphenated.strip("-")
