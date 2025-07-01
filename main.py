from fastapi import FastAPI
from scheduler import start_scheduler

app = FastAPI()
scheduler = start_scheduler()

@app.get("/")
def root():
    return {"message": "Stock notifier backend system started."}

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
    print("Scheduler stopped.")
