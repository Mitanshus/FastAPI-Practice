"""Imported necessary modules needed for Users router."""

import json

from app.curd.users import db_get_user_details
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import get_db



user_router = APIRouter()

# Load environment variables from the .env file
load_dotenv()


@user_router.get("/users", status_code=200)
async def get_users(db: Session = Depends(get_db)):
    """API function for fetching DB users.

    Returns:
    - users_dict: A dictionary containing users data
    """
    try:
        try:
            users_dict = db_get_user_details(db)
        except Exception as e:
            print("Error while fetching users : [%s]", str(e))

            raise HTTPException(
                status_code=500, detail="An error occurred while fetching users."
            ) from e

        print("users fetched : [%s]", json.dumps(users_dict))

        return JSONResponse(
            content=users_dict,
            status_code=200,
        )
    except Exception as e:
        print("Unexpected error : [%s]", str(e))

        raise HTTPException(
            status_code=500, detail="An unexpected error occurred."
        ) from e
