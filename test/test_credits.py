import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import Base, get_db
from main import app
from app.models import CreditLedgers

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

def test_get_expiring_credits(test_db):
    response = client.get("/api/credits?expiry_days=300")
    assert response.status_code == 200
    
    json_response = response.json()
    assert isinstance(json_response, list), f"Expected list, got {type(json_response)}: {json_response}"
    
    # Optional: Check if data exists
    credits = test_db.query(CreditLedgers).filter(CreditLedgers.expiry_date.isnot(None)).all()
    print(f"Database contains {len(credits)} credits with expiry dates")



