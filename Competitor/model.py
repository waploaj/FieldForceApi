from app import db, ma


class Competitor(db.Model):
    __tablename__ = "competitor_info"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, default="", nullable=True)
    holding_stock = db.Column(db.Integer,  default="",  nullable=True)
    selling_stock = db.Column(db.Integer, default="", nullable=True)
    comments = db.Column(db.String(255), nullable=True,  default="")

    def __repr__(self):
        return "<Competitor(id='%s', item_id='%s', holding_stock='%s', selling_stock='%s'>"%(
            self.id, self.item_id, self.holding_stock, self.selling_stock
        )