# skills/emailer.py
import smtplib
from email.mime.text import MIMEText
import config
from core.speaker import speak

def send_email_interactive(speak_func):
    """
    Ask user in terminal for recipient, subject, body and send via Gmail SMTP (requires app password).
    """
    if not config.EMAIL or not config.EMAIL_PASSWORD:
        speak_func("Email is not configured. Put EMAIL and EMAIL_PASSWORD into the .env file.")
        return

    speak_func("Please type the recipient email address in the terminal.")
    to = input("To: ").strip()
    if not to:
        speak_func("No recipient provided.")
        return
    speak_func("Please type the subject now.")
    subject = input("Subject: ").strip()
    speak_func("Please type the message body now.")
    body = input("Body: ").strip()

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config.EMAIL
    msg['To'] = to

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(config.EMAIL, config.EMAIL_PASSWORD)
            server.send_message(msg)
        speak_func("Email sent successfully.")
    except Exception as e:
        print("Email error:", e)
        speak_func("Failed to send the email. Check credentials and network.")
