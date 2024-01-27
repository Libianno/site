from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routes import home

app = FastAPI()

app.mount(
        '/static',
        StaticFiles(directory=Path(__file__).parent.parent.absolute()/'static'),
        name='static'
        )

app.include_router(home.router)

