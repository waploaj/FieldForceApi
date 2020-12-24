from app import ma
from marshmallow import ValidationError
from Posm.model import *


class MaterialSerializer ( ma.SQLAlchemyAutoSchema ) :
    class Meta :
        Model = Material

class PosMaterialSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = PosMaterial

class PosmItemSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = PostMaterial_Item

class RatingSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Rating

class RatingMaterialSerializer( ma.SQLAlchemyAutoSchema ):
    class Meta :
        Model = Rating_Material


def data_not_blank (  data ) :
    if not data :
        raise ValidationError ( "Data is missingg" )
    return True