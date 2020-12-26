from app import db, ma
from datetime import datetime
from sqlalchemy.orm import relationships
from sqlalchemy import ForeignKey


class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), default="", nulllable=False)
    batch_no = db.Column(db.String(255), default="", nullable=False)
    unit = db.Column(db.Integer, default="", nullable=False)
    deleted = db.Column(db.Integer, default="", nullable=False)
    free_product = db.Column(db.Integer, default="", nullable=False)
    item_registration = db.relationships("Item_Registration", backref="item")
    rating_item = db.relationships("Rating_Item", backref="item")


class Registration(db.Model):
    __tablename__ = 'registration'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow )
    item_reg = db.relationships("Item_Registration", backref="registration")

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<Registration(id='%s')>"


class Item_Registration(db.Model):
    __tablename__ = "item_registration"

    id = db.Column(db.Interger, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id", nullable=False))
    latitude = db.Column(db.String(255), default="", nullable=True)
    longitude = db.Column(db.String(255), default="", nullable=True)
    comments = db.Column(db.VARCHAR(255), default="", nullable=True)
    reg_id = db.Column(db.Integer, db.ForeignKey("registration.id"), nullable=False)

    def __repr__(self):
        return "<Item_Registration(id='%s')>" % (self.id)


class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, default="", nullable=False)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Interger, default="", nullable=False)
    rating_material = db.relationships("Rating_Item", backref="rate")

    def __repr__(self):
        return "<Rating(id='%s')>" % (self.id)


class Rating_Item(db.Model):
    __tablename__ = "rating_item"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Interger, default="", nullable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    image = db.Column(db.String(255), default="", nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    rate_id = db.Column(db.Integer, db.ForeignKey("rate.id"), nullable=False)

    def __repr__(self):
        return "<Rating_Item(id='%s')>" % (self.id)


class CompetitorAttendance(db.Model):
    __tablename__ = "Competitor_attendance"

    id = db.Column(db.Interger, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, default="", nulllable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    time = db.Column(db.Datetime, default=datetime.utcnow, onupdate=datetime.utcnow )

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<PostAttendance(id='%s')>" % (self.id)