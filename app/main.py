from pathlib import Path

from fastapi import FastAPI, Request
import logging

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app_dir = Path(__file__).parent
logging.basicConfig(filename=Path(app_dir, 'logs', 'honeypot.log'), encoding='utf-8', level=logging.DEBUG)

app = FastAPI()

app.mount("/static", StaticFiles(directory=Path(app_dir, 'static')), name="static")


@app.get("/")
async def root(request: Request):
    logging.debug(request.client)
    return FileResponse(Path(app_dir, 'index.html'))
