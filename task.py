from config import *
from bdshare import get_current_trade_data
import smtplib
from email.mime.text import MIMEText

# Fetch stock information
def fetch_stock():
    df = get_current_trade_data(STOCK_SYMBOL)
    current_stock_price = df["close"].iloc[0]
    return current_stock_price

# Send email
def send_email(message):
    msg = MIMEText(message)
    msg["Subject"] = f"Daily stock price notifier of {STOCK_SYMBOL}"
    msg["From"] = EMAIL_USER
    msg["To"] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
    
    print("Email sent!")