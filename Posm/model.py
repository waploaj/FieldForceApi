from app import db
from datetime import datetime

class PosMaterial(db.Model):
    __tablename__  =  'posmaterial'

    id = db.Column(db.Integer, primary_key=True)
    item_id =  db.Column(db.Integer, default="", nullable=True)
    latitude = db.Column(db.String(255), default="", nullable=True)
    longitude = db.Column(db.String(255), default="", nullable=True)
    employee_id = db.Column(db.Integer,  nullable=False)
    comments = db.Column(db.VARCHAR(255), default="", nullable=True)
    muda = db.Column(db.DATETIME, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def  __repr__(self):
        return "<PostMaterial(id='%s', item_id='%s', latitude='%s', longitude='%s', employee_id='%s',comment='%s',)>" \
               "muda='%s'"%(
            self.id, self.item_id,self.latitude, self.longitude, self.employee_id, self.comments, self.muda
        )