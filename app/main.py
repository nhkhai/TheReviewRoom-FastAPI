from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import dataloader, start_db
from .api.main import api_router
from .core.config import settings


app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

# Initiate the database, create the tables and load the initial data. 
start_db.main()
dataloader.main()

@app.get("/")
async def root():
    return {"message": "Hello World"}
