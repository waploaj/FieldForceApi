from flask import Blueprint, request, jsonify
from .model import Item
from Utily.auth import token_required
from .serializer import *

comp = Blueprint("comp", __name__ )

@comp.route("/env/", methods=["GET","POST"])
def index():
    if request.method == "POST":
       rm = Item(name = request.json["name"])
    return jsonify(rm)

#TODO: Add business logic here.