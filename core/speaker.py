import pyttsx3
import threading

def speak(text: str):
    """Speak text aloud in a separate thread (non-blocking)."""
    if not text:
        return

    print(f"Saakshi: {text}")

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
