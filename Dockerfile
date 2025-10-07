# ---- Stage 1: Base image ----
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency files first for caching
COPY requirements.txt .

# Install dependencies (and build tools only if needed)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI project
COPY . .

# Expose FastAPI’s default port
EXPOSE 8000

# Start FastAPI using Uvicorn (production-friendly with 0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t fastapi .
# docker run --env-file .env -p 8000:8000 fastapi

# Prevent Python from writing .pyc files and using output buffering
# ENV topStory = 'https://api.thenewsapi.com/v1/news/top'
# ENV allNews = 'https://api.thenewsapi.com/v1/news/all'
# ENV newsByUUID = 'https://api.thenewsapi.com/v1/news/uuid'
# ENV cricketAPI = '9f1ed43a-e8f2-428e-8757-df05f8cced24'
# ENV cricketurl  = 'https://api.cricapi.com/v1'
# ENV theNewsAPIKey = 'iEqu6tqdiMswMusXnFIqR7kZgKK9KOxaCT30I1TU'