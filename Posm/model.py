from app import db
from datetime import datetime
from sqlalchemy.orm import relationships
from sqlalchemy import ForeignKey

class Material(db.Model):
    __tablename__ = "Material"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), default="", nulllable=True)
    batch_no = db.Column(db.String(255), default="", nullable=True)
    unit = db.Column(db.Integer,default="",nullable=True)
    deleted = db.Column(db.Integer, default="", nullable=True)
    free_product = db.Column(db.Integer, default="", nullable=True)
    posm_item = relationships("PostMaterial_Item", backref="material")
    rate_material = relationships("Rating_Material", backref="material")

class PosMaterial(db.Model):
    __tablename__ = 'posmaterial'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=True)
    employee_id = db.Column(db.Integer,  nullable=False)
    time = db.Column(db.DATETIME, default=datetime.utcnow(), onupdate=datetime.utcnow())
    posm_item = relationships("PostMaterial_Item", backref="postmaterial")

    def __init__(self):
        time = self.time = datetime.utcnow()


    def __repr__(self):
        return "<PostMaterial(id='%s', customer_id='%s', employee_id='%s',time='%s',)>" ""\
               %(self.id, self.customer_id,self.employee_id, self.time)

class PostMaterial_Item(db.Model):
    __tablename__  = "postmaterial_item"

    id = db.Column(db.Interger, primary_key=True)
    item_id = db.Column(db.Integer, ForeignKey("material.id"))
    latitude = db.Column(db.String(255), default="", nullable=True)
    longitude = db.Column(db.String(255), default="", nullable=True)
    comments = db.Column(db.VARCHAR(255), default="", nullable=True)
    pos_id = db.Column(db.Integer, ForeignKey("postmaterial.id"))

    def __repr__(self):
        return "<PostMaterial_Item(id='%s')>"%(self.id)


class Rating(db.Model):
    __tablename__ = "pos_ratings"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=True)
    employee_id = db.Column(db.Integer, default="", nullable=True)
    time = db.Column(db.DATETIME, default=datetime.utcnow(), onupdate=datetime.utcnow())
    deleted = db.Column(db.Interger, default="", nullable=True)
    rating_material = relationships("Rating_Material", backref="rate")

    def __repr__(self):
        return "<Rating(id='%s')>"%(self.id)


class Rating_Material(db.Model):
    __tablename__ = "rating_material"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default="", nullable=True)
    latitude = db.Column(db.String(255), default="", nullable=True)
    longitude = db.Column(db.String(255), default="", nullable=True)
    image = db.Column(db.String(255), default="", nullable=True)
    material_id = db.Column(db.Integer, ForeignKey("material.id"))
    rate_id = db.Column(db.Integer, ForeignKey("rate.id"))

    def __repr__(self):
        return "<Rating_Material(id='%s')>"%(self.id)

class PosAttendance(db.Model):
    __tablename__ = "pos_attendance"

    id = db.Column(db.Interger, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, default="", nulllable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    time = db.Column(db.Datetime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<PostAttendance(id='%s')>"%(self.id)