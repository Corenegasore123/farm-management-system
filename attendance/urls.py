from django.urls import path
from .views import add_farmer, attendance_list, students_list, add_student, farmers_list

urlpatterns = [
    path('', farmers_list, name='farmers_list_default'),
    path('farmers/add/', add_farmer, name='add_farmer'),
    path('farmers/', farmers_list, name='farmers_list'),
    path('students/', students_list, name='students_list'),
    path('students/add/', add_student, name='add_student'),
]