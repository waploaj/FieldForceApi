from flask import Blueprint, request, Response
from app import db
from .model import PosMaterial


pos = Blueprint("pos", __name__)

@pos.route("/pos/register", methods=["GET","POST"])
def register_pos():
    """

    :return:
    """
    if request.method == "POST":
        try:
            posm_data = PosMaterial(item_id = request.json["item_id"],
                                    latitude = request.json["latitude"],
                                    longitude = request.json["longitude"],
                                    employee_id = request.json["employee_id"],
                                    # comment = request.json["comment"],
                                    muda =  request.json["muda"]
                                    )

            if posm_data:
                db.session.add(posm_data)
                db.session.commit
            else:
                return "The request is empty!!"

        except  Exception as e:
            print(e)

    else:
        return "Method is not allowed"

    return str( request.json["comment"])