from app import ma
from attendance.model import Attendance
from marshmallow import ValidationError


class AttendanceSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendance

    @staticmethod
    def data_not_blank(data):
        if not data:
            return ValidationError("Data not provide")
        return True
