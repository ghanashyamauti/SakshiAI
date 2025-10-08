# skills/system_control.py
import os
import subprocess
from core.speaker import speak
import config

def system_control(command: str):
    cmd = command.lower()
<<<<<<< HEAD

    # Shutdown
=======
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
    if "shutdown" in cmd:
        speak("Shutting down the computer in 5 seconds.")
        os.system("shutdown /s /t 5")
        return
<<<<<<< HEAD

    # Restart
=======
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
    if "restart" in cmd:
        speak("Restarting the computer in 5 seconds.")
        os.system("shutdown /r /t 5")
        return
<<<<<<< HEAD

    # Lock workstation
=======
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
    if "lock" in cmd:
        speak("Locking the workstation.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return
<<<<<<< HEAD

    # Open applications
    if cmd.startswith("open app") or cmd.startswith("open "):
        # extract app name
=======
    if cmd.startswith("open app") or cmd.startswith("open "):
        # open app by name or try to open the app path
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
        app = cmd.replace("open app", "").replace("open", "").strip()
        if not app:
            speak("Which application should I open?")
            return
<<<<<<< HEAD

        # common apps paths
        common_paths = {
             "brave": config.BRAVE_PATH,
=======
        # try to open common apps or fallback to starting the name
        common_paths = {
            "brave": config.BRAVE_PATH,
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "notepad": "notepad.exe",
            "calculator": "calc.exe"
        }
<<<<<<< HEAD

        path = common_paths.get(app.lower())

        try:
            if path:
                # handle string paths with spaces
                if os.path.isfile(path) or path.endswith(".exe"):
                    subprocess.Popen([path], shell=True)
                else:
                    speak(f"Cannot find the path for {app}.")
            else:
                # fallback to try running app directly
                subprocess.Popen(app, shell=True)
=======
        path = common_paths.get(app.lower())
        try:
            if path:
                subprocess.Popen([path])
            else:
                subprocess.Popen([app])
>>>>>>> 1aa8b79ee4bf33f11bfd95442c2502c5f50276b2
            speak(f"Opening {app}")
        except Exception as e:
            print("Open app error:", e)
            speak("I could not open that application.")
        return

    speak("System command not recognized.")
