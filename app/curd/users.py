"""Imported necessary modules for getting users."""

import json
from sqlalchemy.orm import Session
from datetime import datetime


from app.models import CreditLedgers
from app.models.users import Users

def db_get_user_details(db:Session):
    """Function to fetch user details from the database.
    
    Args:sqlalchymy session object
    
    returns : user details dictionary
    """
    users=db.query(Users).all()

    user_details=[]
    for user in users:
        credits=db.query(CreditLedgers).filter(CreditLedgers.user_id==user.id).first()
        print(credits)
        
        user_details.append({
            "id":user.id,
            "email":user.email,
            "role":user.role,
            "password_set":True if user.password_hash else False,
            "total_creits":credits.total_credits,
            "available_credits":credits.available_credits,
            "credits_expiry":credits.expiry_date.isoformat() if credits.expiry_date else None,
        })
    return user_details


