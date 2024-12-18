"""Imported necessary modules needed for Credit router."""

import json

from app.curd.chats import db_get_chats
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import get_db

chats_router= APIRouter()

# Load environment variables from the .env file
load_dotenv()


@chats_router.get("/chats", status_code=200)
async def get_all_chats(user_id: str = Query(..., description="specific user"), db: Session = Depends(get_db)):
    """API function for fetching DB chats.

    Returns:
    - chats_dict: A dictionary containing chats data
    """
    try:
        try:
            credit_dict = db_get_chats(db, user_id)
            
        except Exception as e:
            print("Error while fetching chats : [%s]", str(e))

            raise HTTPException(
                status_code=500, detail="An error occurred while fetching chats."
            ) from e

        print("chats fetched : [%s]", json.dumps(credit_dict))

        return JSONResponse(
            content=credit_dict,
            status_code=200,
        )
    except Exception as e:
        print("Unexpected error : [%s]", str(e))

        raise HTTPException(
            status_code=500, detail="An unexpected error occurred."
        ) from e
