from sqlalchemy import Integer
from app import db
from datetime import datetime


class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(Integer, primary_key=True)
    check_in = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    check_out = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    employee_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))


    def __repr__(self):
        return "<Attendance(check_ic='%s', check_out='%s', employee_id='%s', customer_id='%s'>" % (
            self.check_in, self.check_out, self.employee_id, self.customer_id)
