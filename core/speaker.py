# core/speaker.py
import pyttsx3

def speak(text: str):
    """Always speak text aloud and print it. Re-initializes engine each time."""
    if not text:
        return

    print(f"Saakshi: {text}")

    try:
        engine = pyttsx3.init()

        # Try to select female voice (Zira)
        voices = engine.getProperty("voices")
        for v in voices:
            if "zira" in v.name.lower():
                engine.setProperty("voice", v.id)
                break

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()  # release resources

    except Exception as e:
        print("TTS error:", repr(e))
