from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from . import dataloader, start_db
from .api.main import api_router
from .core.config import settings


app = FastAPI()

# Set all CORS enabled origins. 
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

# Initialize the database, create the tables and load the initial data. 
start_db.main()
dataloader.main()

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"Message": "The Review Room API is running. "}

@app.get("/health", status_code=status.HTTP_200_OK)
async def get_health():
    return {"Status": "Ok"}