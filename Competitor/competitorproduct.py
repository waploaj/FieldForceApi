from flask import Blueprint, request, jsonify
from app import db
from .model import Competitor
from Utily.auth import token_required
from .serializer import CompetitorSerializer

comp = Blueprint("comp", __name__)

sm = CompetitorSerializer()


@comp.route("/competior", methods=["GET", "POST"])
def upload_competitor_data():
    """

    """
    if request.method == "POST":
        try:
            competitor = Competitor(item_id = request.json["item_id"],
                                    holding_stock = request.json["holding_stock"],
                                    selling_stock = request.json["selling_stock"],
                                    comments= request.json["comments"]

            )
            if sm.data_not_blank(competitor):
                db.session.add(competitor)
                db.session.commit()
                print("okay")
            else:
                raise ValueError("Missing data")
        except Exception as e:
            pass
        return jsonify(200)

@comp.route("/competitor_all", methods=["GET, POST"])
def get_competitor_data():
    """

    """
    if request.method == "POST":
        try:
         result = Competitor.query.all()

        except Exception:
            pass
        results = sm.dump(result, many=True)
    return results




