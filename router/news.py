from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timedelta
from urllib import parse
import os
from router import news


newsRouters = APIRouter(tags=["news"])


# this if for get sport related news
@newsRouters.get('/getNews')
async def getNews(search : str, language :str):
    selectedDate = datetime.now() - timedelta(days=4)
    params = parse.urlencode({
        "api_token" : os.getenv('theNewsAPIKey') ,
        "limit" : 0,
        "published_after" : selectedDate.strftime("%Y-%m-%d"),
        "language" : language,
        "categories" : 'sports',
        "locale" : 'in,pk,',
        'search_fields' : 'title,description,keywords',
        'search' : search
    })
    response = requests.get(f'{os.getenv('allNews') }?{params}')
    if response.status_code == 200:
        return JSONResponse(status_code=200, content=response.json()['data'])
    else:
        return JSONResponse(status_code=400, content={'message' : 'nodata'})
        

@newsRouters.get('/getNewsArticles/{articleId}')
async def getNews(articleId : str):
    params = parse.urlencode({
        "api_token" : os.getenv('theNewsAPIKey') 
    })

    url = f'{os.getenv('newsByUUID') }/{articleId}?{params}'
    response = requests.get(url)
    if response.status_code == 200:
        return JSONResponse(status_code=200, content=response.json())
    else:
        return JSONResponse(status_code=400, content={'message' : 'nodata found'})