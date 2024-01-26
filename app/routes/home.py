from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import json

router = APIRouter()

templates = Jinja2Templates(directory='templates')

@router.get('/')
def home(request: Request, response_class = HTMLResponse):
    with open('animes.json', 'r') as animes:
        animes = animes.read()
        animes = json.loads(animes)

    return templates.TemplateResponse(
        'home.html', {'request':request}, context=animes
    )