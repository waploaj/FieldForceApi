from flask import Blueprint, request, Response
from .model import Attendance
from app import db
from app import create_app
from werkzeug.exceptions import HTTPException


attendance = Blueprint('attendace', __name__)


@attendance.route('/', methods=["GET", "POST"])
def save_employee_attendance():

    if request.method == "POST":
        try:
            em = Attendance(check_in = request.json['check_in'],
                            check_out= request.json["check_out"],
                            latitude = request.json["latitude"],
                            longitude = request.json["longitude"],
                            customer_id = request.json["customer_id"],
                            employee_id = request.json["employee_id"])
            if em:
                db.session.add(em)
                db.session.commit()
            else:
                return "Request  Body is missing"
        except Exception as e:
            pass

    else:
        return Response(status=405)


    return Response(status=200)