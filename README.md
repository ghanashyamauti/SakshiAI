# 🎙️ SakshiAI — Your Personal Desktop Voice Assistant

**SakshiAI** is an intelligent anime-style voice assistant built with **Python** and **AI integration (Cohere API)**.  
It can talk, listen, and help you perform day-to-day computer and web tasks — all through natural speech.

---

## ✨ Features

- ✅ **AI-Powered Conversations** — Uses Cohere AI for natural responses.  
- ✅ **Speech Recognition & Text-to-Speech** — Listens and talks back using `speech_recognition` and `pyttsx3`.  
- ✅ **Smart System Control** — Open apps, control PC, or search the web using voice commands.  
- ✅ **Information Access** — Fetches news, weather, Wikipedia summaries, and more.  
- ✅ **Notes & Email** — Take notes or send emails directly via voice.  
- ✅ **Custom GUI** — Full background image with semi-transparent conversation box.  
- ✅ **Stop Command** — Say “stop” anytime to immediately stop the assistant from speaking.

---

## 🧠 Core Modules

| Folder / File        | Description |
|---------------------|-------------|
| `core/brain.py`      | Main decision engine routing queries to correct actions. |
| `core/speaker.py`    | Handles text-to-speech with instant stop support. |
| `core/cohere_ai.py`  | Integrates Cohere API for open-ended conversation. |
| `skills/`            | Individual skill modules (weather, notes, system control, etc.). |
| `gui.py`             | Main application GUI with background and chat interface. |
| `.env`               | Stores API keys (Cohere, OpenWeather, etc.). |
| `config.py`          | Configuration and environment variable loader. |

---

## 🖥️ GUI Overview

- Background image: `saakshi.png` (704 × 978 pixels)  
- Title at the top: “SaakshiAI – Your Voice Companion”  
- Conversation area at the bottom (semi-transparent)  
- Start/Stop buttons below the chat box  

---

## 🧩 Requirements

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
