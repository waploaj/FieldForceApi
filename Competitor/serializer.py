from app import ma
from Competitor.model import Competitor
from marshmallow import ValidationError

class CompetitorSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        Model  = Competitor

    def data_not_blank(self, data):
        if not data:
            raise ValidationError("Data is missingg")
