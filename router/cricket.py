from fastapi import APIRouter
from fastapi.responses import JSONResponse
from urllib import parse
import os
from dotenv import load_dotenv
import requests

load_dotenv()

cricketRouters = APIRouter()    


@cricketRouters.get('/cricket/series', tags=["cricket"])
async def getCricket():
    params = parse.urlencode({
        "apikey" : os.getenv('cricketAPI'), 
        "offset" : 0 
    })

    url = f'{os.getenv('cricketurl') }/series?{params}'
    response = requests.get(url)
    if response.status_code == 200:
        return JSONResponse(status_code=200, content=response.json()['data'][:6])
    else:
        return JSONResponse(status_code=400, content={'message' : 'nodata found'})


@cricketRouters.get('/cricket/matches', tags=["cricket"])
async def getCricket():
    params = parse.urlencode({
        "apikey" : os.getenv('cricketAPI'), 
        "offset" : 0 
    })

    url = f'{os.getenv('cricketurl') }/matches?{params}'
    response = requests.get(url)
    if response.status_code == 200:
        return JSONResponse(status_code=200, content=response.json()['data'][:6])
    else:
        return JSONResponse(status_code=400, content={'message' : 'nodata found'})