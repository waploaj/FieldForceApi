from app import ma
from Competitor.model import (Item,
                              Registration,
                              Item_Registration,
                              Rating,
                              Rating_Item)
from marshmallow import ValidationError


class ItemSerializer ( ma.SQLAlchemyAutoSchema ) :
    class Meta :
        Model = Item

class RegistrationSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Registration

class Item_RegistrationSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Item_Registration

class RatingSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Rating

class Rating_ItemSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Rating_Item


def data_not_blank (  data ) :
    if not data :
        raise ValidationError ( "Data is missingg" )
    return True
