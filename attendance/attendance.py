from flask import Blueprint

attendance = Blueprint('attendace', __name__)

@attendance.route('/', methods=["GET"])
def save_employee_attendance():
    return "200"