# skills/system_control.py
import os
import subprocess
from core.speaker import speak
import config

def system_control(command: str):
    cmd = command.lower()
    if "shutdown" in cmd:
        speak("Shutting down the computer in 5 seconds.")
        os.system("shutdown /s /t 5")
        return
    if "restart" in cmd:
        speak("Restarting the computer in 5 seconds.")
        os.system("shutdown /r /t 5")
        return
    if "lock" in cmd:
        speak("Locking the workstation.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return
    if cmd.startswith("open app") or cmd.startswith("open "):
        # open app by name or try to open the app path
        app = cmd.replace("open app", "").replace("open", "").strip()
        if not app:
            speak("Which application should I open?")
            return
        # try to open common apps or fallback to starting the name
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
                subprocess.Popen([path])
            else:
                subprocess.Popen([app])
            speak(f"Opening {app}")
        except Exception as e:
            print("Open app error:", e)
            speak("I could not open that application.")
        return

    speak("System command not recognized.")
