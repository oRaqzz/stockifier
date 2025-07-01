from dotenv import load_dotenv
import os 

load_dotenv()

STOCK_SYMBOL = os.getenv("STOCK_SYMBOL")
SCHEDULE_HOUR = int(os.getenv("SCHEDULE_HOUR"))
SCHEDULE_MINUTE = int(os.getenv("SCHEDULE_MINUTE"))

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")


