# skills/notes.py
import time
import config
<<<<<<< HEAD
import threading
from core.speaker import speak

NOTES_FILE = getattr(config, "NOTES_FILE", "notes.txt")


def manage_notes(command: str):
    """
    Handles all note-related commands:
    - Add/write notes
    - Show/list notes
    - Set reminders
    """
    cmd = command.lower()

    # 1. Add / write note
    if any(k in cmd for k in ("write", "add", "remember", "note", "take a note")) and "show" not in cmd:
        speak("What should I write in the note? Please type it in the terminal.")
        note = input("Note: ").strip()

        if note:
            with open(NOTES_FILE, "a", encoding="utf-8") as f:
=======
from core.speaker import speak

def manage_notes(command: str):
    cmd = command.lower()
    # Add / write note
    if any(k in cmd for k in ("write", "add", "remember", "note", "take a note")) and "show" not in cmd:
        speak("What should I write in the note? Please type it in the terminal.")
        note = input("Note: ").strip()
        if note:
            with open(config.NOTES_FILE, "a", encoding="utf-8") as f:
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
                f.write(f"{time.ctime()} - {note}\n")
            speak("Note saved.")
        else:
            speak("No text provided, note cancelled.")
<<<<<<< HEAD
        return "Note action complete."

    # 2. Show or list notes
    if any(k in cmd for k in ("show", "list", "read")):
        try:
            with open(NOTES_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()

            if not data:
                speak("You have no notes.")
                return "No notes found."

            speak("Here are your recent notes. I will also print them in the terminal.")
            print("\n--- NOTES ---")
            print(data)
            print("-------------\n")
            return "Notes listed."
        except FileNotFoundError:
            speak("You have no notes yet.")
            return "No notes file found."

    # 3. Simple reminders: "remind me to X in 2 minutes"
=======
        return

    # Show or list notes
    if any(k in cmd for k in ("show", "list", "read")):
        try:
            with open(config.NOTES_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()
            if not data:
                speak("You have no notes.")
                return
            speak("Here are your recent notes. I will also print them in the terminal.")
            print("--- NOTES ---")
            print(data)
            return
        except FileNotFoundError:
            speak("You have no notes yet.")
            return

    # Remind simple: "remind me to X in 2 minutes" - basic parsing
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
    if "remind me to" in cmd and " in " in cmd:
        try:
            what = cmd.split("remind me to", 1)[1].split(" in ", 1)[0].strip()
            num_unit = cmd.split(" in ", 1)[1].strip()
<<<<<<< HEAD

            num = int(num_unit.split()[0])  # e.g., "2 minutes"
            unit = num_unit.split()[1]
            seconds = num * (60 if unit.startswith("minute") else 1)

            speak(f"Reminder set for {num} {unit}. I will notify you in the terminal.")

            def _job():
                time.sleep(seconds)
                speak(f"Reminder: {what}")

            threading.Thread(target=_job, daemon=True).start()
            return f"Reminder set for {what}"
        except Exception as e:
            print("Reminder parse error:", e)
            speak("I could not set the reminder. Try: remind me to <task> in 2 minutes.")
            return "Reminder failed."

    # 4. Fallback
    speak("Notes command not recognized.")
    return "Notes command not recognized."
=======
            # e.g., "2 minutes"
            num = int(num_unit.split()[0])
            unit = num_unit.split()[1]
            seconds = num * (60 if unit.startswith("minute") else 1)
            speak(f"Reminder set for {num} {unit}. I will notify you in the terminal.")
            # spawn a simple delayed notification thread
            import threading, time
            def _job():
                time.sleep(seconds)
                speak(f"Reminder: {what}")
            threading.Thread(target=_job, daemon=True).start()
        except Exception as e:
            print("Reminder parse error:", e)
            speak("I could not set the reminder. Try: remind me to <task> in 2 minutes.")
        return

    # fallback
    speak("Notes command not recognized.")
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
