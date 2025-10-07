from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from router import news, cricket
from fastapi.responses import JSONResponse


load_dotenv()

app = FastAPI()

origins = [
    "http://sportbet-insk.netlify.app/",
    "https://sportbet-insk.netlify.app",
    "www.sportbet-insk.netlify.app/",
    "http://localhost:3000",
    "https://localhost:3000",
    "https://sportbet-insk.netlify.app/",
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

app.include_router(news.newsRouters, prefix="/api")
app.include_router(cricket.cricketRouters, prefix="/api")
