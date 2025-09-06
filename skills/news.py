# skills/news.py
import requests
import config
from core.speaker import speak

def top_headlines():
    api = config.NEWSAPI_KEY
    if not api:
        return ["News API key not set in .env."]
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api}"
    try:
        r = requests.get(url, timeout=6).json()
        arts = r.get("articles", [])
        titles = [a.get("title", "") for a in arts if a.get("title")]
        return titles or ["No headlines found."]
    except Exception as e:
        print("News error:", e)
        return ["News service is not responding."]
