import pyttsx3
import threading

# Global flag to control speaking
stop_speaking = False
current_engine = None

def speak(text: str):
    """Speak text aloud in a separate thread (non-blocking) and print it."""
    global stop_speaking, current_engine

    if not text:
        return

    print(f"Saakshi: {text}")
    stop_speaking = False  # Reset stop flag before starting

    def run_tts():
        global stop_speaking, current_engine
        try:
            engine = pyttsx3.init()
            current_engine = engine

            # Try to select female voice (Zira)
            voices = engine.getProperty("voices")
            for v in voices:
                if "zira" in v.name.lower():
                    engine.setProperty("voice", v.id)
                    break

            engine.setProperty("rate", 170)
            engine.setProperty("volume", 1.0)

            engine.say(text)
            engine.startLoop(False)

            while engine.isBusy():
                if stop_speaking:
                    engine.stop()
                    break
                engine.iterate()

            engine.endLoop()
            engine.stop()  # release resources
            current_engine = None

        except Exception as e:
            print("TTS error:", repr(e))

    threading.Thread(target=run_tts, daemon=True).start()


def stop_voice():
    """Immediately stop Saakshi’s speech."""
    global stop_speaking, current_engine
    stop_speaking = True
    if current_engine:
        try:
            current_engine.stop()
        except Exception:
            pass
