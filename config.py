import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Wake word
WAKE_WORD = os.getenv("WAKE_WORD", "sakshi")

# Brave browser executable path (Windows). 
BRAVE_PATH = os.getenv(
    "BRAVE_PATH",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
)

# API keys
COHERE_API_KEY = os.getenv("COHERE_API_KEY", "")   # ✅ Added this
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")

# Email for sending (use Gmail app password recommended)
EMAIL = os.getenv("EMAIL", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

# Ensure data folder exists
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Data files
NOTES_FILE = os.getenv("NOTES_FILE", os.path.join(DATA_DIR, "notes.txt"))
LOG_FILE = os.getenv("LOG_FILE", os.path.join(DATA_DIR, "logs.txt"))
