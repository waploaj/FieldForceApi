from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME,DECIMAL
from app import db
from  datetime import datetime

Base = declarative_base()

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String(255))
    batch_no = db.Column(db.String(255))
    unit = db.Column(db.Integer)
    deleted = db.Column(db.Integer)
    free_product = db.Column(db.Integer)
    item_registration = db.relationship("Item_Registration", backref="item")
    rating_item = db.relationship("Rating_Item", backref="item")

    def __repr__(self):
        return "<Item(id='%s', name='%s', batch_no='%s' \
               >"%(self.id, self.name)

class Registration(db.Model):
    __tablename__ = 'registration'

    id = db.Column(Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow )
    item_reg = db.relationship("Item_Registration", backref="registration")

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<Registration(id='%s', customer_id='%s', employee_id='%s')>"


class Item_Registration(db.Model):
    __tablename__ = "item_registration"

    id = db.Column(Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    comments = db.Column(db.VARCHAR(255))
    reg_id = db.Column(db.Integer, db.ForeignKey("registration.id"))

    def __repr__(self):
        return "<Item_Registration(id='%s')>" % (self.id)


class Rating(db.Model):
    __tablename__ = "rates"

    id = db.Column(Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(Integer, default=0, nullable=False)
    rating_materials = db.relationship("Rating_Item", backref="ratecomp")

    def __repr__(self):
        return "<Rating(id='%s')>" % (self.id)


class Rating_Item(db.Model):
    __tablename__ = "rating_item"

    id = db.Column(Integer, primary_key=True)
    rate = db.Column(Integer)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    image = db.Column(db.String(255), default="default.svg", nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    rate_id = db.Column(db.Integer, db.ForeignKey("rates.id"), nullable=False)

    def __repr__(self):
        return "<Rating_Item(id='%s')>" % (self.id)


class CompetitorAttendance(db.Model):
    __tablename__ = "Competitor_attendance"

    id = db.Column(Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    time = db.Column(DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow )

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<PostAttendance(id='%s')>" % (self.id)