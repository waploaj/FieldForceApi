from app import db
from sqlalchemy import Integer, VARCHAR, String, DATETIME
from datetime import datetime


class Survery(db.Model):
    __tablename__ = "survey"

    id = db.Column(db.Integer, primary_key=True)
    qns = db.Column(VARCHAR(255), nullable=True)
    group_qns_id =  db.Column(Integer,nullable=True)
    type = db.Column(Integer, default="", nullable=True)
    time = db.Column(DATETIME, default=datetime.utcnow(), onupdate=datetime.utcnow())
    address = db.Column(String, default="", nullable=True)

    def __repr__(self):
        return "<qns='%s>"%(self.qns)
