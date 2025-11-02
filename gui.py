import sys
import threading
import time
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from core.listener import take_command
from core.brain import process_command
from core.speaker import speak
from core.speaker import speak, stop_voice

class SaakshiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saakshi - Personal Voice Assistant 🎀")
        # Set GUI size to match saakshi.png dimensions
        self.setFixedSize(704, 978)
        self.listening = False
        self.initUI()
        self.greet_user()  # Greeting at startup

    def initUI(self):
        # --- Set full background ---
        self.set_background("assets/saakshi.png")

        # --- Main vertical layout ---
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # --- Title at top ---
        self.title = QLabel("💫 Saakshi - Your Anime AI Assistant 💫", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.title.setStyleSheet(
            "color: white; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px;"
        )
        layout.addWidget(self.title)

        # Spacer pushes chat box to bottom
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # --- Conversation box at bottom ---
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            font-size: 14px;
            color: white;
            background: rgba(0, 0, 0, 0.35);
            border-radius: 12px;
            padding: 8px;
        """)
        self.output.setFixedHeight(250)
        layout.addWidget(self.output)

        # --- Buttons below chat ---
        button_layout = QHBoxLayout()
        self.listen_btn = QPushButton("🎤 Start Listening", self)
        self.listen_btn.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            color: white;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4CAF50, stop:1 #81C784);
            border-radius: 10px;
        """)
        self.listen_btn.clicked.connect(self.start_listening)
        button_layout.addWidget(self.listen_btn)

        self.stop_btn = QPushButton("🛑 Stop", self)
        self.stop_btn.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            color: white;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #E53935, stop:1 #EF5350);
            border-radius: 10px;
        """)
        self.stop_btn.clicked.connect(self.stop_listening)
        button_layout.addWidget(self.stop_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def set_background(self, image_path):
        pixmap = QPixmap(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setPalette(palette)

    def greet_user(self):
        # Time-based dynamic greeting
        hour = datetime.now().hour
        if hour < 12:
            greeting_time = "Good morning"
        elif 12 <= hour < 18:
            greeting_time = "Good afternoon"
        else:
            greeting_time = "Good evening"

        greeting = f"{greeting_time}! Hii Ghanashyam, I’m Saakshi, your personal AI assistant."
        self.output.append(f"Saakshi: {greeting}\n")
        threading.Thread(target=lambda: speak(greeting), daemon=True).start()

    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.output.append("Saakshi: Listening...\n")
            threading.Thread(target=self.listen_loop, daemon=True).start()

    def stop_listening(self):
        self.listening = False
        self.output.append("Saakshi: Stopped listening.\n")
        speak("Stopped listening.")

    def listen_loop(self):
        while self.listening:
            query = take_command()
            if not query:
                continue
            self.output.append(f"You: {query}\n")
            response = process_command(query)  # <-- uses full brain.py logic
            if response:
                self.output.append(f"Saakshi: {response}\n")
                speak(response)
            if any(word in query for word in ["stop", "exit", "goodbye"]):
                self.listening = False
                stop_voice()  # Immediately stop current speech
                self.output.append("Saakshi: Goodbye!\n")
                speak("Goodbye! See you soon!")
                break
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SaakshiApp()
    window.show()
    sys.exit(app.exec_())
