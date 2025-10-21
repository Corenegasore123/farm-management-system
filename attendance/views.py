from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FarmerForm, StudentForm
from .models import Attendance, Student, Farmer


def add_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmer saved successfully.')
            return redirect('add_farmer')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerForm()
    return render(request, 'attendance/add_farmer.html', {'form': form})


def students_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/students_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved successfully.')
            return redirect('students_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    return render(request, 'attendance/add_student.html', {'form': form})


def attendance_list(request):
    attendances = Attendance.objects.select_related('farmer').all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})


def farmers_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'attendance/farmers_list.html', {'farmers': farmers})