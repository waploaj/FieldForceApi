from flask import Blueprint, request, Response
from .model import Attendance
from app import db
from .serializer import AttendanceSerializer
from flask import jsonify
from Utily.auth import token_required



attendance = Blueprint('attendance', __name__)


@attendance.route("/1", methods=["POST"])
@token_required
def save_employee_attendance():
    """
    insert only single attendance
    param:
        check_in: time start visit
        check_out: time take to leave
        employee_id: employee id
        customer_id: customer id
        latitude: latitude coordinate to the visit
        longitude: longitude coordinate to the visit
    return:
        status code from server
    """
    if request.method == "POST" and request.json:
        try:
            attend = Attendance(check_in=request.json["check_in"],
                                check_out=request.json['check_out'],
                                employee_id=request.json["employee_id"],
                                customer_id=request.json["customer_id"],
                                latitude=request.json["latitude"],
                                longitude=request.json["longitude"])
            db.session.add(attend)
            db.session.commit()
        except Exception as e:
            return e
    else:
        return Response(status=405), {"Message": "Method not allowed :)"}


@attendance.route("/", methods=["POST"])
@token_required
def save_employees_attendances():
    """
    insert multiple attendance
    param:
        check_in: time start visit
        check_out: time take to leave
        employee_id: employee id
        customer_id: customer id
        latitude: latitude coordinate to the visit
        longitude: longitude coordinate to the visit
    return:
        status code from server
    """
    if request.method == "POST":
        try:
            for req in request.json:
                attend = Attendance(check_in=req["check_in"],
                                    check_out=req["check_out"],
                                    employee_id=req["employee_id"],
                                    customer_id=req["customer_id"],
                                    latitude=req["latitude"],
                                    longitude=req["longitude"]
                                    )
                if attend:
                    db.session.add(attend)
                    db.session.commit()
                    return Response(status=200), {"Message": "Method not allowed :) "}
                else:
                    return jsonify(Response(status=500), {"Message": "Some parameter are missing :)"})
            return jsonify(Response(status=200))
        except Exception as e:
            return e
    else:
        return jsonify(Response(status=405), {"Message": "Method not allowed :)"})
