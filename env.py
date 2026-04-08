from fastapi import FastAPI
from env import StudentEnv

app = FastAPI()
env = StudentEnv()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/reset")
def reset():
    return env.reset().dict()