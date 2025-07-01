from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from config import *
from task import fetch_stock, send_email

def start_scheduler():
    scheduler = BackgroundScheduler()

    def daily_task():
        price = fetch_stock()
        msg = f"Today's price of {STOCK_SYMBOL}: {price}"
        send_email(msg)
        print("Daily task executed")

    trigger = CronTrigger(hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE)
    scheduler.add_job(daily_task, trigger)

    scheduler.start()
    print("📅 Scheduler started!")
    return scheduler
