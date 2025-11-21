from fastapi import FastAPI
from .routers import tasks  # import the tasks router

app = FastAPI()

# Include the tasks router so its endpoints become active
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Tasks API with error handling and validation"}
