from app import ma
from attendance.model import Attendance

class AttendanceSerializer(ma.Schema):
    class Meta:

        model = Attendance

        fields = ("check_in", "check_out", "latitude", "longitude")
