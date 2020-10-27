from flask import Blueprint, request, Response
from .model import Attendance
from app import db
import jsonify



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
                print("mambo poa")
            else:
                return "Request  Body is missing"
        except Exception as e:
            pass

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
    return str(employee)


@attendance.route("/employee", methods=["GET", "POST"])
def get_by_employee_id():
    """

    :param employee_id:
    :return:
    """
    if request.method == "POST":
        try:
            employee_data = Attendance(employee_id = request.json["employee_id"])
        except Exception as e:
            pass
    else:
        return Response(status=405)

    return str(Attendance.query.filter(Attendance == employee_data))


