# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Wake word
WAKE_WORD = os.getenv("WAKE_WORD", "sakshi")

# Brave browser executable path (Windows). Keep %s or without doesn't matter for BackgroundBrowser.
BRAVE_PATH = os.getenv(
    "BRAVE_PATH",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
)

# API keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")

# Email for sending (Gmail app password recommended)
EMAIL = os.getenv("EMAIL", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

# Data files
NOTES_FILE = os.getenv("NOTES_FILE", "data/notes.txt")
LOG_FILE = os.getenv("LOG_FILE", "data/logs.txt")
