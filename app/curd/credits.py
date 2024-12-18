"""Imported necessary modules for getting credits."""

import json
from sqlalchemy.orm import Session
from datetime import datetime


from app.models import CreditLedgers


def db_get_expiring_credits(db:Session,days:int):
    """Function to fetch credits details from the database.
    
    Args:sqlalchymy session object
    
    returns : credits details dictionary
    """
    credits = db.query(CreditLedgers).all()
    expiring_credit=[]
    for credit in credits:
        if credit.expiry_date:
            if (credit.expiry_date.date() - datetime.now().date()).days <= days:
                expiring_credit.append({
                    "user_id":credit.user_id,
                    "user":credit.user.email,
                    "available_credits":credit.available_credits,
                    "expiry_date":credit.expiry_date.isoformat() if credit.expiry_date else None
                })

    return expiring_credit


