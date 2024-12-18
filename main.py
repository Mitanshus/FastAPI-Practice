"""Imported necessary models to initialize FastAPI server."""

import os

import uvicorn
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, HTTPException, Request, logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers.users import user_router

# Load environment variables from the .env file
load_dotenv()

# Access the "port" environment variable
port: int = int(os.getenv("PORT", "4000"))
origins = os.getenv("ORIGIN", '["http://localhost:5173"]')

# creating fastapi app
app = FastAPI()

# main entry point
main_router = APIRouter()

# Include your routers
app.include_router(main_router)
app.include_router(user_router, prefix="/api", tags=["users"])



# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(_request: Request, exc: HTTPException):
    """Handle HTTP errors raised during request processing."""
    return JSONResponse(
        content={
            "message": exc.detail,
        },
        status_code=exc.status_code,
    )


def runserver():
    """Function to run FastAPI server."""
    logger.debug("Starting FastAPI server on %s",port)
    uvicorn.run("app.main:app", port=port, reload=True)
