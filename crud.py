from sqlalchemy.orm import Session
from sqlalchemy import inspect, Table, MetaData

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

def authenticate_user(username: str, password: str, db: Session):
    # Replace with your user authentication logic
    user = db.query(users).filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_token({"user_id": user.id})
        return token
    return None