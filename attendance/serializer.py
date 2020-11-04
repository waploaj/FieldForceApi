from app import ma
from attendance.attendance import Attendance
from marshmallow import ValidationError


class AttendanceSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendance

        def data_not_blank(self, data):
            if not data:
                raise ValidationError("Data not provide")



