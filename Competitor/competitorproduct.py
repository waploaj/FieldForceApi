from flask import Blueprint, request, Response
from app import db
from Utily.auth import token_required
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
            if competitor:
                db.session.add(competitor)
                db.session.commit()
                print("okay")
            else:
                raise ValueError("Missing data")
        except Exception as e:
            pass
        return Response(200)

@comp.



