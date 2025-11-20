from fastapi import FastAPI
from .routers import tasks

app = FastAPI()

# Includes the tasks router
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Tasks API (structured version)"}
