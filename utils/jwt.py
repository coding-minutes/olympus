import jwt
from typing import Dict, Any
from olympus.config import Config


def encode(data: Dict[str, Any]):
    encoded = jwt.encode(data, Config.JWT_SECRET)
    return encoded


def decode(token: str):
    decoded = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
    return decoded
