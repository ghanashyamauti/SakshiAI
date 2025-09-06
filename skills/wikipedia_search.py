# skills/wikipedia_search.py
import wikipedia

def summary(topic: str) -> str:
    if not topic:
        return "Please tell me a topic to search on Wikipedia."
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        print("Wikipedia error:", e)
        return "Sorry, I couldn't fetch Wikipedia results right now."
