from fastapi import FastAPI
from starlette import responses

app = FastAPI()
@app.get("/ping")
def ping():
    return responses.JSONResponse({"message": "pong"})
