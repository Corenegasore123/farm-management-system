from django.contrib import admin
from attendance.models import Farmer, Attendance, Student, StudentAttendance


# Register your models here.
admin.site.register(Farmer)
admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(StudentAttendance)
