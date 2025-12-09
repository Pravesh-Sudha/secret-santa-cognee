# matcher.py
import cognee
from cognee import SearchType
import re
import asyncio
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Allowed emotion keywords (lowercase)
EMOTIONS = ["happy", "stressed", "lonely", "excited", "neutral"]

def _normalize_search_result(result):
    """
    Turn various cognee.search return shapes into a single text string.
    Handles:
      - list of strings
      - list of dicts (take first dict and any 'answer'/'text'/'content' keys)
      - dict with 'answer'/'text' keys
      - raw string (just return)
    """
    if result is None:
        return ""

    # If it's a list
    if isinstance(result, list):
        if len(result) == 0:
            return ""
        first = result[0]

        # list of simple strings
        if isinstance(first, str):
            return " ".join([str(x) for x in result if isinstance(x, str)])

        # list of dict-like objects: try to extract common fields
        if isinstance(first, dict):
            # try to find a key that likely contains the answer
            for key in ("answer", "text", "content", "result", "output"):
                if key in first and isinstance(first[key], str):
                    return first[key]

            # if dict keys are nested or different, try join any string values in dict
            string_vals = []
            for item in result:
                if isinstance(item, dict):
                    for v in item.values():
                        if isinstance(v, str):
                            string_vals.append(v)
            if string_vals:
                return " ".join(string_vals)

        # fallback: stringify first element
        return str(first)

    # If it's a dict
    if isinstance(result, dict):
        for key in ("answer", "text", "content", "result", "output"):
            if key in result and isinstance(result[key], str):
                return result[key]

        # If some nested values exist, join string values
        string_vals = [str(v) for v in result.values() if isinstance(v, str)]
        if string_vals:
            return " ".join(string_vals)

        # fallback to stringified dict
        return str(result)

    # If it's a plain string
    if isinstance(result, str):
        return result

    # Anything else: just stringify
    return str(result)


async def detect_emotions(name):
    """
    Query cognee for the emotional state of `name` and return one of EMOTIONS.
    This function is robust to different return types from cognee.search.
    """
    query = f"What is the emotional state or mood of {name}?"
    try:
        result = await cognee.search(query_text=query, query_type=SearchType.RAG_COMPLETION)
    except Exception as e:
        log.exception("cognee.search() raised an exception")
        return "neutral"

    # Debug: log raw result so you can inspect shapes during development
    log.info("Raw cognee.search result for %s: %s", name, repr(result))

    text = _normalize_search_result(result).lower().strip()
    log.info("Normalized answer text: %s", text)

    # Simple keyword match first
    for emo in EMOTIONS:
        if re.search(rf"\b{re.escape(emo)}\b", text):
            return emo

    # Fuzzy checks (e.g., "anxious" -> stressed; "sad" -> lonely/stressed)
    if re.search(r"\banxious\b|\banxiety\b|\bstress(ed)?\b|\boverwhelmed\b", text):
        return "stressed"
    if re.search(r"\balone\b|\blonely\b|\bisolat(e|ed)\b|\bmiss my friends\b", text):
        return "lonely"
    if re.search(r"\b(excited|thrill|pumped|enthusiast)\b", text):
        return "excited"
    if re.search(r"\b(happy|joy|great|amazing|celebrat)\b", text):
        return "happy"

    # If nothing matches, safe fallback
    return "neutral"


def match_friends(friends):

    rules = {
        "happy": ["stressed", "lonely"],
        "excited": ["neutral"],
        "stressed": ["happy"],
        "lonely": ["happy"],
        "neutral": ["happy", "excited"]
    }

    available = friends.copy()
    assignments = {}

    import random

    for giver in friends:
        possible = [
            f for f in available
            if f["name"] != giver["name"] and f["emotion"] in rules[giver["emotion"]]
        ]

        if not possible:
            possible = [f for f in available if f["name"] != giver["name"]]

        receiver = random.choice(possible)
        assignments[giver["name"]] = receiver["name"]
        available.remove(receiver)

    return assignments
