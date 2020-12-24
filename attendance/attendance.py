from flask import Blueprint, request, Response, jsonify
from attendance.model import Attendance
from attendance.serializer import AttendanceSerializer
from app import db, loggger, app
from Utily.auth import token_required

sm = AttendanceSerializer()
lists = []
att = Blueprint('attendace', __name__)


@att.route('/checkin', methods = ["GET", "POST"])
@token_required
def save_employee_attendance():
    if request.method == "POST":
        lists.append(request.json)
        for list in list:
            list = Attendance(check_in = request.json['check_in'],
                            check_out = request.json["check_out"],
                            latitude = request.json["latitude"],
                            longitude = request.json["longitude"],
                            customer_id = request.json["customer_id"],
                            employee_id = request.json["employee_id"])

            if list:
                    db.session.add(list)
                    db.session.commit()
            else:
                return "Missing parameters"

    else:
        return Response(status = 405), loggger.info("bad request")
    return Response(status = 200)


@att.route("/all", methods = ["GET", "POST"])
@token_required
def get_all_attendance():
    """

    :return:
    """
    if request.method == "POST":
        try:
            employee = Attendance.query.all()
            result = sm.dump(employee, many = True)

        except Exception as e:
            print(e)
        return jsonify(result)
    else:
        return jsonify(app.logger.info("badahdjkajfka hfahadkh"))

@att.route("/employee", methods = ["GET", "POST"])
@token_required
def get_by_employee_id():
    """



    :return:
    """
    if request.method == "POST":
        try:

            data = Attendance.query.filter(Attendance.employee_id == request.json["employee_id"])
        except Exception as e:
            print(e)
        if data:
            result =sm.dump(data, many = True)
        return jsonify(result)
