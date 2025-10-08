<<<<<<< HEAD
=======
# main.py
import time
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
import config
from core.listener import take_command
from core.speaker import speak
from core.brain import process_command

def main():
    speak("Hi Ghanashaam I am Saakshi, your personal AI assistant.")
    while True:
<<<<<<< HEAD
        # keep listening
=======
        # listen
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
        query = take_command()
        if not query:
            continue
        q = query.lower()

<<<<<<< HEAD
        # exit commands
=======
        # exit
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
        if any(k in q for k in ("stop", "exit", "quit", "bye")):
            speak("Goodbye, see you soon!")
            break

<<<<<<< HEAD
        # process query
=======
        # process -> returns a string response (or None)
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
        response = process_command(q)
        if response:
            speak(response)

<<<<<<< HEAD
        # ❌ removed time.sleep(2) → now talk + listen overlap
=======
        # IMPORTANT: wait so TTS finishes and mic doesn't immediately capture it
        time.sleep(2)
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2

if __name__ == "__main__":
    main()
