import config
from core.listener import take_command
from core.speaker import speak
from core.brain import process_command

def main():
    speak("Hi Ghanashaam I am Saakshi, your personal AI assistant.")
    while True:
        # keep listening
        query = take_command()
        if not query:
            continue
        q = query.lower()

        # exit commands
        if any(k in q for k in ("stop", "exit", "quit", "bye")):
            speak("Goodbye, see you soon!")
            break

        # process query
        response = process_command(q)
        if response:
            speak(response)

        # ❌ removed time.sleep(2) → now talk + listen overlap

if __name__ == "__main__":
    main()
