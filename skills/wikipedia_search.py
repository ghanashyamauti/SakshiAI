# skills/wikipedia_search.py
import wikipedia

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
