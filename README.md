# stockifier

Your daily stock price email notifier, built with FastAPI + Python.

## Features
- Fetches daily stock price using bdshare
- Sends email at a fixed time every day
- Configurable via `.env` file
- Deployable to Render to run 24/7

## Local setup
```
Clone the repo and install dependencies:
git clone https://github.com/oRaqzz/stockifier.git
cd stockifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:
```env
STOCK_SYMBOL=YourStockSymbol
SCHEDULE_HOUR=HourToNotify
SCHEDULE_MINUTE=MinuteToNotify
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your@gmail.com
EMAIL_PASSWORD=your_app_password
TO_EMAIL=recipient@gmail.com
```

Enable 2FA on your Google account, then go to:
https://myaccount.google.com/apppasswords
Generate an app password for "Mail" → copy it into .env.
paste it to -> EMAIL_PASSWORD.

## Run locally

uvicorn main:app --reload
Visit: http://127.0.0.1:8000

## Deploy to Render (24/7)
```
Push code to GitHub
On Render: New → Web Service → connect repo
Build command: pip install -r requirements.txt
Start command: uvicorn main:app --host 0.0.0.0 --port 10000
Add environment variables in Render
```
Click Deploy!!
