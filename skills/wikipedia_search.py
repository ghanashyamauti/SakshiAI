# skills/wikipedia_search.py
import wikipedia

<<<<<<< HEAD
def search_wikipedia(query):
    """
    Search Wikipedia and return a summary of the query.
    """
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Your query is too broad. Options include: {e.options[:5]}"
    except wikipedia.PageError:
        return "I couldn't find anything on Wikipedia for that topic."
    except Exception as e:
        return f"Error while searching Wikipedia: {str(e)}"
=======
def summary(topic: str) -> str:
    if not topic:
        return "Please tell me a topic to search on Wikipedia."
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        print("Wikipedia error:", e)
        return "Sorry, I couldn't fetch Wikipedia results right now."
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
