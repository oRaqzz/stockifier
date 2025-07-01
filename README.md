stockifier
==========
Your daily stock price email notifier, built with FastAPI + Python.

Features
--------
- Fetches daily stock price using bdshare
- Sends email at a fixed time every day
- Configurable via .env file
- Deployable to Render to run 24/7

Local setup
-----------
Clone the repo and set up:
bash
git clone https://github.com/oRaqzz/stockifier.git
cd stockifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

**create an .env file with**
-----------
* STOCK_SYMBOL="Your stock symbol"
SCHEDULE_HOUR="the hour you want to be notified"
SCHEDULE_MINUTE="the minute you want to be notifed"

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
TO_EMAIL=recipient@gmail.com

enable 2FA on your google account and go to this link -> https://myaccount.google.com/apppasswords 
type "Mail" and get your password!

**Running the server**
Navigate to your file and type "uvicorn main:app --reload" in terminal 

if you want to run it 24/7 deploy it on render!

Push your code to GitHub
Go to Render → New Web Service → Connect repo
Build command: pip install -r requirements.txt
Start command: uvicorn main:app --host 0.0.0.0 --port 10000
Add environment variables in Render dashboard

Click Deploy
