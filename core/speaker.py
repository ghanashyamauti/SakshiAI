<<<<<<< HEAD
import pyttsx3
import threading

def speak(text: str):
    """Speak text aloud in a separate thread (non-blocking)."""
=======
# core/speaker.py
import pyttsx3

def speak(text: str):
    """Always speak text aloud and print it. Re-initializes engine each time."""
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
    if not text:
        return

    print(f"Saakshi: {text}")

<<<<<<< HEAD
    def run_tts():
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

    # Run speaking in background so listening continues
    threading.Thread(target=run_tts, daemon=True).start()
=======
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
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
