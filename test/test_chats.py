import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import Base, get_db
from main import app
from app.models.chats import Chats

SQLALCHEMY_DATABASE_URL = "postgresql://GenRPT:TEA@localhost/genrptdbtest"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    db = TestingSessionLocal()
    yield db
    db.close()

def test_get_all_chats(test_db):
    response = client.get("/api/chats", params={"user_id":"24fcd43f-60e7-4d9c-8a6f-193a046ef4fc"})
    assert response.status_code == 200
    
    # Debug print
    print(f"Response content: {response.content}")
    print(f"Response type: {type(response.json())}")
    
    json_response = response.json()
    assert isinstance(json_response, list), f"Expected list, got {type(json_response)}: {json_response}"
    
    # Optional: Check if data exists
    chats = test_db.query(Chats).filter_by(user_id="24fcd43f-60e7-4d9c-8a6f-193a046ef4fc").all()
    print(f"Database contains {len(chats)} chats for this user")

def test_get_specific_chat(test_db):
    # Using existing data
    response = client.get("/api/chats/3e1ad4d9-29ad-4c3f-b5fd-baa37dc5d0ce")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)