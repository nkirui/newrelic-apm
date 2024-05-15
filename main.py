import uvicorn
from fastapi import FastAPI
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware
from logger import logger
import asyncio


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

logger.info("Starting APi ----")


@app.get("/")
async def index() -> dict:
    return {"message": "World"}


# simulate long  processing task
@app.get("/upload_video")
async def upload_videoas() -> dict:
    await asyncio.sleep(1.5)
    return {"message": 'Video Uploaded successfully'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # produdction:❯  newrelic-admin run-program uvicorn main:app --host 0.0.0.0 --port 80
