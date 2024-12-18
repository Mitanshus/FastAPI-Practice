"""Imported necessary modules needed for Credit router."""

import json

from app.curd.credits import db_get_expiring_credits
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import get_db



credits_router= APIRouter()

# Load environment variables from the .env file
load_dotenv()


@credits_router.get("/credits", status_code=200)
async def get_expiring_credits(expiry_days: int = Query(..., description="Number of days until credits expire"), db: Session = Depends(get_db)):
    """API function for fetching DB credits.

    Returns:
    - credits_dict: A dictionary containing credits data
    """
    try:
        try:
            credit_dict = db_get_expiring_credits(db, expiry_days)
        except Exception as e:
            print("Error while fetching credits : [%s]", str(e))

            raise HTTPException(
                status_code=500, detail="An error occurred while fetching credits."
            ) from e

        print("credits fetched : [%s]", json.dumps(credit_dict))

        return JSONResponse(
            content=credit_dict,
            status_code=200,
        )
    except Exception as e:
        print("Unexpected error : [%s]", str(e))

        raise HTTPException(
            status_code=500, detail="An unexpected error occurred."
        ) from e
