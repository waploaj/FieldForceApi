from flask import Blueprint, request, jsonify
from .model import *


pos = Blueprint("pos", __name__)

@pos.route("/pos/register", methods=["GET","POST"])
def register_pos():
    """

    :return:
    """

    if request.method == "POST":
        for req in request.json:
            registration = PosMaterial(customer_id = req["customer_id"],
                                       employee_id = req["employee_id"]
                                       )
            if registration:
                pass
            registred_posm = PostMaterial_Item(item_id=req["item_id"],
                                               latitude=req["latitude"],
                                               longitude=req["longitude"],
                                               comments=req["comments"],
                                               pos_id=req["pos_id"]
                                               )
            if registred_posm:
                pass

    else:
        return "Method is not allowed"

    return jsonify(200)