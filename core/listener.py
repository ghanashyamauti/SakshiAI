# core/listener.py
import speech_recognition as sr
from core.speaker import speak

def take_command(timeout: int = 6) -> str:
    """
    Listen on the default microphone for `timeout` seconds and return recognized text.
    Returns empty string on failure.
    """
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, phrase_time_limit=timeout)
    except Exception as e:
        print("Microphone error:", e)
        speak("Microphone not available.")
        return ""

    try:
        text = r.recognize_google(audio, language="en-in")
        print("You:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network error for speech recognition.")
        return ""
