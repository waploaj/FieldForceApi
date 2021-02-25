from app import app, db
import jwt
from flask import Blueprint, request, Response, jsonify
import datetime

utilty = Blueprint("utilty", __name__)


@utilty.route("/login", methods=["GET", "POST"])
def auth_encoding():
    try:
        if request.method == "POST":
            person_id = request.args.get("person_id")
            if person_id:
                payload = {
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=86400),
                    "iat": datetime.datetime.utcnow(),
                    "sub": person_id
                }

                token = jwt.encode(payload, app.config["SECRET_KEY"])
                print(token)

                return Response(token.decode("UTF-8"))

            return Response({"Message": "Error on authenticate"})

        return Response({"Message": "Method not Allowed "}, status=405)

    except Exception as e:
        print(e)

    return Response(status=200)