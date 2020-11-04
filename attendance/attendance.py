from flask import Blueprint, request, Response
from attendance.model import Attendance
from attendance.serializer import AttendanceSerializer
from app import db
import jsonify
from Utily.auth import token_required



sm = AttendanceSerializer()
att = Blueprint('attendace', __name__)

@token_required
@att.route('/', methods=["GET", "POST"])
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
                db.session.add(em)
                db.session.commit()

            else:
                return "Request  Body is missing"
       except Exception as e:
            print(e)

    else:
        return Response(status=405)
    return Response(status=200)



@att.route("/all", methods=["GET", "POST"])
def get_all_attendance():
    """

    :return:
    """
    if request.method  == "POST" or "GET":
        try:
            employee = Attendance().query.all()

        except Exception as e:
            pass

        result =sm.dump(employee, many=True)
        print(employee)
    else:
        return "Method not allowed",Response(405)
    return str(result)


@att.route("/employee", methods=["GET", "POST"])
def get_by_employee_id():
    """

    :param employee_id:
    :return:
    """
    data = ""
    if request.method == "POST":
        try:

            data = Attendance.query.filter(Attendance.employee_id == request.json["employee_id"])
        except Exception as e:
            pass
        if data:
            result = sm.dump(data, many=True)
        return str(result)





