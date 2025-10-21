from django.urls import path
from .views import (add_farmer, attendance_list, students_list, add_student, 
                    farmers_list, mark_attendance, edit_farmer, delete_farmer,
                    edit_student, delete_student, edit_attendance, delete_attendance,
                    dashboard, export_attendance_csv, bulk_mark_attendance,
                    farmer_list_json, student_list_json, view_farmer, view_student)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('attendance/', attendance_list, name='attendance_list'),
    path('attendance/export/', export_attendance_csv, name='export_attendance'),
    path('attendance/bulk-mark/', bulk_mark_attendance, name='bulk_mark_attendance'),
    path('farmers/', farmers_list, name='farmers_list'),
    path('farmers/add/', add_farmer, name='add_farmer'),
    path('farmers/<int:pk>/', view_farmer, name='view_farmer'),
    path('farmers/<int:pk>/edit/', edit_farmer, name='edit_farmer'),
    path('farmers/<int:pk>/delete/', delete_farmer, name='delete_farmer'),
    path('farmers/json/', farmer_list_json, name='farmer_list_json'),
    path('students/', students_list, name='students_list'),
    path('students/add/', add_student, name='add_student'),
    path('students/<int:pk>/', view_student, name='view_student'),
    path('students/<int:pk>/edit/', edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', delete_student, name='delete_student'),
    path('students/json/', student_list_json, name='student_list_json'),
    path('students/attendance/mark/', mark_attendance, name='mark_attendance'),
    path('attendance/<int:pk>/edit/', edit_attendance, name='edit_attendance'),
    path('attendance/<int:pk>/delete/', delete_attendance, name='delete_attendance'),
]