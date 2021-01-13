from flask import Blueprint, request, jsonify
from Posm.model import Material, PosMaterial, PostMaterial_Item, Rating, Rating_Material


pos = Blueprint("pos", __name__)
#TODO: Add Business Logic Here!!