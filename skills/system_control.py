# skills/system_control.py
import os
import subprocess
from core.speaker import speak
import config

def system_control(command: str):
    cmd = command.lower()

    # Shutdown
    if "shutdown" in cmd:
        speak("Shutting down the computer in 5 seconds.")
        os.system("shutdown /s /t 5")
        return

    # Restart
    if "restart" in cmd:
        speak("Restarting the computer in 5 seconds.")
        os.system("shutdown /r /t 5")
        return

    # Lock workstation
    if "lock" in cmd:
        speak("Locking the workstation.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return

    # Open applications
    if cmd.startswith("open app") or cmd.startswith("open "):
        # extract app name
        app = cmd.replace("open app", "").replace("open", "").strip()
        if not app:
            speak("Which application should I open?")
            return

        # common apps paths
        common_paths = {
             "brave": config.BRAVE_PATH,
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "notepad": "notepad.exe",
            "calculator": "calc.exe"
        }

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
            speak(f"Opening {app}")
        except Exception as e:
            print("Open app error:", e)
            speak("I could not open that application.")
        return

    speak("System command not recognized.")
