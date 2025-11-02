# main.py
import time
import config
from core.listener import take_command
from core.speaker import speak
from core.brain import process_command

def main():
    speak("Hi Ghanashyam, I am Saakshi, your personal AI assistant.")
    while True:
        # Listen for a voice command
        query = take_command()
        if not query:
            continue
        q = query.lower()

        # Exit commands
        if any(k in q for k in ("stop", "exit", "quit", "bye")):
            speak("Goodbye, see you soon!")
            break

        # Process the spoken command and get a response
        response = process_command(q)
        if response:
            speak(response)

        # Wait so TTS finishes before listening again
        time.sleep(2)

if __name__ == "__main__":
    main()
