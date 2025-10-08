from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from router import news, cricket
from fastapi.responses import JSONResponse


load_dotenv()

app = FastAPI()

origins = [
    "https://8jjsport.com.in", 
    "https://8jjsport.com.in/",
    "http://8jjsport.com.in", 
    "http://8jjsport.com.in/",
    "https://8jjsport.com.in/",
    "http://8jjsport.com.in/",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news.newsRouters,)
app.include_router(cricket.cricketRouters,)
