Stockifier
Your daily stock price email notifier, built with FastAPI + Python.

Features
Fetches daily stock prices using bdshare.

Sends emails at a fixed time every day.

Configurable via a .env file.

Deployable to Render to run 24/7.

Local Setup
To set up Stockifier locally, follow these steps:

Clone the repository:

Bash

git clone https://github.com/oRaqzz/stockifier.git
cd stockifier
Set up a virtual environment and install dependencies:

Bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Create an .env file:
Create a file named .env in the root directory of the project and add the following configuration:

STOCK_SYMBOL="Your stock symbol"
SCHEDULE_HOUR="the hour you want to be notified"
SCHEDULE_MINUTE="the minute you want to be notifed"

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
TO_EMAIL=recipient@gmail.com
Note for Gmail users: To get your EMAIL_PASSWORD, you need to enable 2-Factor Authentication (2FA) on your Google account. Then, visit https://myaccount.google.com/apppasswords, select "Mail" as the app, and generate an app password.

Running the Server
Once configured, navigate to your project directory in the terminal and run the server using Uvicorn:

Bash

uvicorn main:app --reload
Deployment to Render (24/7)
To deploy Stockifier on Render and have it run continuously, follow these steps:

Push your code to GitHub.

Go to Render:

Log in to your Render account.

Click on New Web Service.

Connect your GitHub repository.

Configure the build and start commands:

Build command: pip install -r requirements.txt

Start command: uvicorn main:app --host 0.0.0.0 --port 10000

Add environment variables:
Add the environment variables from your .env file to the Render dashboard's environment variables section.

Click Deploy.
