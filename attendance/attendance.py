from flask import Blueprint, request, Response
from attendance.model import Attendance
from app import db
import jsonify
from Utily.auth import token_required
from attendance.serializer import AttendanceSerializer as schema


sm = schema()
attendance = Blueprint('attendace', __name__)

@token_required
@attendance.route('/', methods=["GET", "POST"])
def save_employee_attendance():

    if request.method == "POST":
       em = Attendance(check_in=request.json['check_in'],
                   check_out=request.json["check_out"],
                   latitude=request.json["latitude"],
                   longitude=request.json["longitude"],
                   customer_id=request.json["customer_id"],
                   employee_id=request.json["employee_id"])
       try:

            if em:
                db.Session.add(em)
                db.Session.commit()
                print("mambo poa")
                sm.dump(em)

            else:
                return "Request  Body is missing"
       except Exception as e:
            print(e)

    else:
        return Response(status=405)

    return Response(status=200)



@attendance.route("/all", methods=["GET", "POST"])
def get_all_attendance():
    """

    :return:
    """
    try:
        employee = Attendance.query.all()
    except Exception as e:
        pass
    return sm.dump(employee)


@attendance.route("/employee", methods=["GET", "POST"])
def get_by_employee_id():
    """

    :param employee_id:
    :return:
    """
    if request.method == "POST":
        try:
            employee_data = Attendance(employee_id = request.json["employee_id"])
            data = Attendance.query.filter(Attendance == employee_data)
        except Exception as e:
            pass
    else:
        return Response(status=405)

    return sm.dump(data)


