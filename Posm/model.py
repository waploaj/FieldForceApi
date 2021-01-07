from app import db
from datetime import datetime

class Material(db.Model):
    __tablename__ = "Material"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), default="", nulllable=False)
    batch_no = db.Column(db.String(255), default="", nullable=False)
    unit = db.Column(db.Integer,default="",nullable=False)
    deleted = db.Column(db.Integer, default="", nullable=False)
    free_product = db.Column(db.Integer, default="", nullable=False)
    posm_item = db.relationship("PosMaterial_Item", backref="material")
    rate_material = db.relationship("Rating_Material", backref="material")

class PosMaterial(db.Model):
    __tablename__ = 'posmaterial'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer,  nullable=False)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow )
    posm_item = db.relationship("PostMaterial_Item", backref="postmaterial")

    def __init__(self):
        time = self.time = datetime.utcnow()


    def __repr__(self):
        return "<PostMaterial(id='%s', customer_id='%s', employee_id='%s',time='%s',)>" ""\
               %(self.id, self.customer_id,self.employee_id, self.time)

class PostMaterial_Item(db.Model):
    __tablename__  = "postmaterial_item"

    id = db.Column(db.Interger, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    comments = db.Column(db.VARCHAR(255), default="", nullable=False)
    pos_id = db.Column(db.Integer, db.ForeignKey("postmaterial.id"), nullable=False)

    def __repr__(self):
        return "<PostMaterial_Item(id='%s')>"%(self.id)


class Rating(db.Model):
    __tablename__ = "pos_ratings"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, default="", nullable=False)
    time = db.Column(db.DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow )
    deleted = db.Column(db.Interger, default=1, nullable=False)
    rating_material = db.relationship("Rating_Material", backref="rate")

    def __repr__(self):
        return "<Rating(id='%s')>"%(self.id)


class Rating_Material(db.Model):
    __tablename__ = "rating_material"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=0, nullable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    image = db.Column(db.String(255), default="default.svg", nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), nullable=False)
    rate_id = db.Column(db.Integer, db.ForeignKey("rate.id"), nullable=False)

    def __repr__(self):
        return "<Rating_Material(id='%s')>"%(self.id)

class PosAttendance(db.Model):
    __tablename__ = "pos_attendance"

    id = db.Column(db.Interger, primary_key=True)
    customer_id = db.Column(db.Integer, default="", nullable=False)
    employee_id = db.Column(db.Integer, default="", nulllable=False)
    latitude = db.Column(db.String(255), default="", nullable=False)
    longitude = db.Column(db.String(255), default="", nullable=False)
    time = db.Column(db.Datetime, default=datetime.utcnow, onupdate=datetime.utcnow )

    def __init__(self):
        self.time = datetime.utcnow()

    def __repr__(self):
        return "<PostAttendance(id='%s')>"%(self.id)