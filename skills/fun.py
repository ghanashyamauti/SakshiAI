# skills/fun.py
import pyjokes

def random_joke() -> str:
    try:
        return pyjokes.get_joke()
    except Exception:
        return "I couldn't fetch a joke right now."
