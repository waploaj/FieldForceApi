from app import db
from flask_login import UserMixin
from datetime import datetime
from  werkzeug.security import generate_password_hash, check_password_hash


class Userapi(db.Model, UserMixin):
    __tablename__ =  "person"

    person_id  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), default = "", nullable = True)
    token = db.Column(db.String(255), nullable = True)
    password = db.Column(db.String(255), nullable = True)
    registered = db.Column(db.DateTime, onupdate = datetime.utcnow(), default = datetime.utcnow())

    def __init__(self, name, token, password, registerd):
        self.name  = name
        self.token = token
        self.password = generate_password_hash(password)
        self.registered = datetime.utcnow()

    def __repr__(self):
        return f"<Person {self.name}>"

    def verify_password( self, pwd ):
        return check_password_hash(self.password, pwd)