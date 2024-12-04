import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_token(data, expires_in=600):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(seconds=expires_in)
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None