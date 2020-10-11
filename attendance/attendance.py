from flask import Blueprint, request
from .model import Attendance
from app import db



attendance = Blueprint('attendace', __name__)

@attendance.route('/', methods=["GET", "POST"])
def save_employee_attendance(employee_data):
    if request.methods == "POST":
        em = Attendance(check_in = request.json['check_in'],
                        check_out= request.json["check_out"],
                        latitude = request.json["latitude"],
                        longitude = request.json["longitude"],
                        customer_id = request.json["customer_id"],
                        employee_id = request.json["employee_id"])
        db.session.add(em)
        db.session.commit()

    return "200"