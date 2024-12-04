from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import authenticate_user, get_items

app = FastAPI()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return get_items(db)


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    token = authenticate_user(username, password, db)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": token}