# skills/weather.py
import requests
import config
from core.speaker import speak

def get_weather(command: str):
    api = config.OPENWEATHER_API_KEY
    if not api:
        speak("OpenWeather API key is not set. Put it in the .env file.")
        return

    # Try to get city from "weather in <city>"
    city = "Pune"
    if " in " in command:
        city = command.split(" in ", 1)[1].strip()
    # call API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    try:
        r = requests.get(url, timeout=6).json()
        if r.get("cod") != 200:
            speak(f"I couldn't find weather for {city}.")
            return
        desc = r["weather"][0]["description"].capitalize()
        temp = r["main"]["temp"]
        feels = r["main"].get("feels_like")
        speak(f"{desc} in {city}. Temperature is {temp:.0f}°C, feels like {feels:.0f}°C.")
    except Exception as e:
        print("Weather error:", e)
        speak("Weather service is not responding right now.")
