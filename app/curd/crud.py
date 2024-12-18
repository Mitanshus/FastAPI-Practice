from sqlalchemy.orm import Session
from sqlalchemy import inspect, Table, MetaData

from app.models.users import Users
from jwt_utils import create_token

def get_items(db: Session):
    inspector = inspect(db.get_bind())
    tables = inspector.get_table_names()
    all_items = {}
    metadata = MetaData()

    for table_name in tables:
        table = Table(table_name, metadata, autoload_with=db.get_bind())
        query = db.query(table).all()
        all_items[table_name] = [row._asdict() for row in query]

    return all_items

def authenticate_user(email: str, password: str, db: Session):
    users = db.query(Users).all()
    user = db.query(users).filter_by(email=email).first()
    if user and user.check_password(password):
        token = create_token({"user_id": user.id})
        return token
    return None