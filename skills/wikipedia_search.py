# skills/wikipedia_search.py
import wikipedia

def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia and return a short summary of the query.
    """
    if not query:
        return "Please tell me a topic to search on Wikipedia."

    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Your query is too broad. Options include: {e.options[:5]}"
    except wikipedia.PageError:
        return "I couldn't find anything on Wikipedia for that topic."
    except Exception as e:
        print("Wikipedia error:", e)
        return "Sorry, I couldn't fetch Wikipedia results right now."
