from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first API!"}

@app.get("/hello")
def say_hello():
    return {"greeting": "Hello, User!"}

@app.get("/python")
def say_day():
    return {"python": "The main file is written in python"}
