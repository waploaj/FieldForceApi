from app import app
from flask import request
import jwt

import datetime

def auth_encoding(person_id):
    try:
        payload ={
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days = 1),
            "iat": datetime.datetime.utcnow(),
            "sub": person_id
        }
        token = jwt.encode(payload, app.config["SECRET_KEY"])
        return token.decode("UTF-8")
    except Exception as e:
        return e
(auth_encoding(1))
