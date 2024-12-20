"""Imported necessary modules for getting chats."""

import json
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.chats import Chats
from enum import Enum


def db_get_chats(db: Session, chat_id: str = None):
    """Function to fetch chats details from the database.
    
    Args:
        db (Session): SQLAlchemy session object
        chat_id (str, optional): ID of the chat to fetch. Defaults to None.
    
    Returns:
        str: JSON string of chat details.
    """
    chats = db.query(Chats).all() if not chat_id else db.query(Chats).filter(Chats.id == chat_id).all()
    chat_dicts = [chat.__dict__ for chat in chats if hasattr(chat, '__dict__')]
    
    for chat_dict in chat_dicts:
        chat_dict.pop('_sa_instance_state', None)
    
    return jsonable_encoder(chats)



def db_get_specific_chats(db:Session,chat_id:str):
    """Function to fetch credits details from the database.
    
    Args:sqlalchymy session object
    
    returns : credits details dictionary
    """
    chat = db.query(Chats).filter(Chats.id == chat_id).first()
    if chat:
        return jsonable_encoder(chat)
    else:
        return {}


