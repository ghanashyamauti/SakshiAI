import webbrowser
import os
import pywhatkit

# Register Brave browser
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
if os.path.exists(brave_path):
    webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path))

def open_youtube():
    """Open YouTube in Brave browser."""
    try:
        webbrowser.get("brave").open("https://www.youtube.com")
        return "Opening YouTube in Brave browser."
    except:
        webbrowser.open("https://www.youtube.com")  # fallback
        return "Opening YouTube in default browser."

def search_web(query):
    """Google search in Brave browser."""
    try:
        webbrowser.get("brave").open(f"https://www.google.com/search?q={query}")
        return f"Here are the Google search results for {query}."
    except:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Here are the Google search results for {query}."

def play_youtube_song(song_name):
    """Play a song on YouTube automatically using pywhatkit."""
    try:
        pywhatkit.playonyt(song_name)  # opens first YouTube result in default browser
        return f"Playing '{song_name}' on YouTube."
    except Exception as e:
        return f"Sorry, I couldn't play '{song_name}' on YouTube. Error: {e}"
