from app import ma
from .model import Attendance

class AttendanceSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = Attendance

    check_in = ma.auto_field()
    check_out = ma.auto_field()
    employee_id = ma.auto_field()
    customer_id = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
