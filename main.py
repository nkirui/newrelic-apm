from typing import Union
import uvicorn
from fastapi import FastAPI
from logger import logger

app = FastAPI()

logger.info("Starting APi ----")


@app.get("/")
async def index() -> dict:
    logger.info("Hello world dict")
    return {"message": "World"}


@app.get("/upload_videos")
async def upload_videoas() -> dict:
    logger.info("debug is also working")
    return {"message": 'Vedeo Uploaded'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)