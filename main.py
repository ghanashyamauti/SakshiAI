# main.py
import time
import config
from core.listener import take_command
from core.speaker import speak
from core.brain import process_command

def main():
    speak("Hi Ghanashaam I am Saakshi, your personal AI assistant.")
    while True:
        # listen
        query = take_command()
        if not query:
            continue
        q = query.lower()

        # exit
        if any(k in q for k in ("stop", "exit", "quit", "bye")):
            speak("Goodbye, see you soon!")
            break

        # process -> returns a string response (or None)
        response = process_command(q)
        if response:
            speak(response)

        # IMPORTANT: wait so TTS finishes and mic doesn't immediately capture it
        time.sleep(2)

if __name__ == "__main__":
    main()
