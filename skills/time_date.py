from datetime import datetime

def tell_date():
    return datetime.now().strftime("%A, %d %B %Y")

def tell_time():
    return datetime.now().strftime("%I:%M %p")
