# core/brain.py
<<<<<<< HEAD

from core.cohere_ai import get_cohere_response
=======
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
import skills.time_date as time_date
import skills.wikipedia_search as wikipedia_search
import skills.web_search as web_search
import skills.weather as weather
import skills.news as news
import skills.notes as notes
import skills.emailer as emailer
import skills.system_control as system_control
import skills.fun as fun

def process_command(query: str):
    """Decide what to do based on the spoken query."""
    query = query.lower()

    # ✅ Personality responses
    if "your name" in query:
        return "My name is Sakshi, your personal AI assistant."

    elif "who are you" in query or "what are you" in query:
        return "I am Sakshi, an AI created to assist you with daily tasks."

    elif "how are you" in query or ("how" in query and "you" in query):
        return "I am always good when I am helping you!"

    elif "thank you" in query or "thanks" in query:
        return "You're welcome! Happy to help."

    # ✅ Time and date
    elif "time" in query and "date" in query:
        return f"The time is {time_date.tell_time()} and today's date is {time_date.tell_date()}"
    
    elif "time" in query:
        return f"The time is {time_date.tell_time()}"

    elif "date" in query:
        return f"Today's date is {time_date.tell_date()}"

    # ✅ Wikipedia search
    elif "wikipedia" in query:
        return wikipedia_search.search_wikipedia(query)

    # ✅ Web search / YouTube
    elif "play" in query and "youtube" in query:
<<<<<<< HEAD
=======
        # Extract song name
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
        song_name = query.replace("play", "").replace("on youtube", "").strip()
        if song_name:
            web_search.play_youtube_song(song_name)
            return f"Playing '{song_name}' on YouTube."
        else:
            return "Please tell me the song name you want to play on YouTube."

    elif "youtube" in query or "open youtube" in query:
        web_search.open_youtube()
        return "Opening YouTube in Brave browser."

    elif "search" in query:
        web_search.search_web(query)
        return f"Searching for '{query}' on the web."

    # ✅ Other skills
    elif "weather" in query:
        return weather.get_weather(query)

    elif "news" in query:
        return news.get_news()

<<<<<<< HEAD
    elif any(k in query for k in ("note down", "take a note", "write note", "remind")):
        return notes.manage_notes(query)
=======
    elif "note" in query:
        return notes.take_note()
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2

    elif "email" in query:
        return emailer.send_email()

<<<<<<< HEAD
    elif any(k in query for k in ("shutdown", "restart", "lock", "open app", "open notepad", "open calculator", "open brave", "open chrome", "open vscode")):
        return system_control.system_control(query)
=======
    elif "shutdown" in query or "restart" in query:
        return system_control.system_action(query)
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2

    elif "joke" in query or "fun" in query:
        return fun.tell_joke()

<<<<<<< HEAD
    # ✅ Fallback to Cohere AI
    else:
        return get_cohere_response(query)
=======
    # ✅ Fallback response
    else:
        return "Sorry, I didn’t understand that. Can you repeat?"
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
