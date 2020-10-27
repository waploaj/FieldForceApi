from app import db
from datetime import datetime
from sqlalchemy import Integer, String, DATETIME, VARCHAR

class PosMaterial(db.Model):
    __tablename__  =  'posmaterial'

    id = db.Column(Integer, primary_key=True)
    item_id =  db.Column(Integer, default="", nullable=True)
    latitude = db.Column(String(255), default="", nullable=True)
    longitude = db.Column(String(255), default="", nullable=True)
    employee_id = db.Column(Integer,  nullable=False)
    comments = db.Column(VARCHAR(255), default="", nullable=True)
    muda = db.Column(DATETIME, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def  __repr__(self):
        return "<PostMaterial(id='%s', item_id='%s', latitude='%s', longitude='%s', employee_id='%s',comment='%s',)>" \
               "muda='%s'"%(
            self.id, self.item_id,self.latitude, self.longitude, self.employee_id, self.comments, self.muda
        )