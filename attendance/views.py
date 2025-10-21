from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from django.db.models import Count, Q
from .forms import FarmerForm, StudentForm
from .models import Attendance, Student, Farmer, StudentAttendance
from django.utils import timezone
from datetime import date as _date, timedelta
from django.http import HttpResponse, JsonResponse
import csv


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
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            models.Q(name__icontains=search_query) |
            models.Q(class_name__icontains=search_query) |
            models.Q(school__icontains=search_query)
        )
    
    # Filter by school
    school_filter = request.GET.get('school', '')
    if school_filter:
        students = students.filter(school__icontains=school_filter)
    
    # Filter by class
    class_filter = request.GET.get('class', '')
    if class_filter:
        students = students.filter(class_name__icontains=class_filter)
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'name')
    if sort_by in ['name', 'class_name', 'age', 'school', '-name', '-class_name', '-age', '-school']:
        students = students.order_by(sort_by)
    
    # Get unique schools and classes for filter dropdowns
    schools = Student.objects.values_list('school', flat=True).distinct().order_by('school')
    classes = Student.objects.values_list('class_name', flat=True).distinct().order_by('class_name')
    
    context = {
        'students': students,
        'search_query': search_query,
        'school_filter': school_filter,
        'class_filter': class_filter,
        'schools': schools,
        'classes': classes,
        'sort_by': sort_by,
    }
    return render(request, 'attendance/students_list.html', context)


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student "{student.name}" updated successfully.')
            return redirect('students_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'attendance/edit_student.html', {'form': form, 'student': student})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f'Student "{name}" deleted successfully.')
        return redirect('students_list')
    return render(request, 'attendance/confirm_delete.html', {'object': student, 'type': 'student'})


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
    """View all student attendance records with filters."""
    # Get all student attendance records
    attendance_records = StudentAttendance.objects.select_related('student').all()
    
    # Date filter
    date_filter = request.GET.get('date', '')
    if date_filter:
        try:
            filter_date = _date.fromisoformat(date_filter)
            attendance_records = attendance_records.filter(date=filter_date)
        except Exception:
            pass
    
    # Status filter
    status_filter = request.GET.get('status', '')
    if status_filter == 'present':
        attendance_records = attendance_records.filter(is_present=True)
    elif status_filter == 'absent':
        attendance_records = attendance_records.filter(is_present=False)
    
    # Student filter
    student_filter = request.GET.get('student', '')
    if student_filter:
        attendance_records = attendance_records.filter(student__name__icontains=student_filter)
    
    # Sort by date (newest first)
    attendance_records = attendance_records.order_by('-date', 'student__name')
    
    # Get unique dates for filter
    dates = StudentAttendance.objects.values_list('date', flat=True).distinct().order_by('-date')[:30]
    
    context = {
        'attendance_records': attendance_records,
        'date_filter': date_filter,
        'status_filter': status_filter,
        'student_filter': student_filter,
        'dates': dates,
    }
    return render(request, 'attendance/attendance_list.html', context)


def farmers_list(request):
    farmers = Farmer.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        farmers = farmers.filter(
            models.Q(name__icontains=search_query) |
            models.Q(farm__icontains=search_query) |
            models.Q(location__icontains=search_query)
        )
    
    # Filter by location
    location_filter = request.GET.get('location', '')
    if location_filter:
        farmers = farmers.filter(location__icontains=location_filter)
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'name')
    if sort_by in ['name', 'farm', 'age', 'location', '-name', '-farm', '-age', '-location']:
        farmers = farmers.order_by(sort_by)
    
    # Get unique locations for filter dropdown
    locations = Farmer.objects.values_list('location', flat=True).distinct().order_by('location')
    
    context = {
        'farmers': farmers,
        'search_query': search_query,
        'location_filter': location_filter,
        'locations': locations,
        'sort_by': sort_by,
    }
    return render(request, 'attendance/farmers_list.html', context)


def edit_farmer(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Farmer "{farmer.name}" updated successfully.')
            return redirect('farmers_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerForm(instance=farmer)
    return render(request, 'attendance/edit_farmer.html', {'form': form, 'farmer': farmer})


def delete_farmer(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    if request.method == 'POST':
        name = farmer.name
        farmer.delete()
        messages.success(request, f'Farmer "{name}" deleted successfully.')
        return redirect('farmers_list')
    return render(request, 'attendance/confirm_delete.html', {'object': farmer, 'type': 'farmer'})


def mark_attendance(request):
    """Mark student attendance for a specific date (default today)."""
    if request.method == 'POST':
        # date may come from the form, else default to today
        date_str = request.POST.get('date')
        try:
            date = _date.fromisoformat(date_str) if date_str else timezone.now().date()
        except Exception:
            date = timezone.now().date()

        # expected POST keys: present_<student_id> = 'on'
        students = Student.objects.all()
        count_present = 0
        for s in students:
            present = request.POST.get(f'present_{s.id}') == 'on'
            obj, _ = StudentAttendance.objects.get_or_create(date=date, student=s, defaults={'is_present': present})
            if obj.is_present != present:
                obj.is_present = present
                obj.save()
            if present:
                count_present += 1
        messages.success(request, f'Attendance saved for {date}. Present: {count_present}/{students.count()}')
        return redirect('mark_attendance')

    # GET: render form for today or selected date
    date_str = request.GET.get('date')
    try:
        date = _date.fromisoformat(date_str) if date_str else timezone.now().date()
    except Exception:
        date = timezone.now().date()

    students = list(Student.objects.all())
    # preload attendance state for the date
    existing = {sa.student_id: sa.is_present for sa in StudentAttendance.objects.filter(date=date)}
    rows = [(s, existing.get(s.id, False)) for s in students]
    context = {
        'rows': rows,
        'date': date,
    }
    return render(request, 'attendance/mark_attendance.html', context)


def edit_attendance(request, pk):
    """Edit a single attendance record."""
    attendance = get_object_or_404(StudentAttendance, pk=pk)
    if request.method == 'POST':
        is_present = request.POST.get('is_present') == 'on'
        attendance.is_present = is_present
        attendance.save()
        messages.success(request, f'Attendance for {attendance.student.name} on {attendance.date} updated successfully.')
        return redirect('attendance_list')
    
    context = {
        'attendance': attendance,
    }
    return render(request, 'attendance/edit_attendance.html', context)


def delete_attendance(request, pk):
    """Delete a single attendance record."""
    attendance = get_object_or_404(StudentAttendance, pk=pk)
    if request.method == 'POST':
        student_name = attendance.student.name
        date = attendance.date
        attendance.delete()
        messages.success(request, f'Attendance record for {student_name} on {date} deleted successfully.')
        return redirect('attendance_list')
    
    context = {
        'attendance': attendance,
    }
    return render(request, 'attendance/confirm_delete_attendance.html', context)


def dashboard(request):
    """Dashboard with statistics and overview."""
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    
    # Basic counts
    total_students = Student.objects.count()
    total_farmers = Farmer.objects.count()
    
    # Today's attendance
    today_attendance = StudentAttendance.objects.filter(date=today)
    today_present = today_attendance.filter(is_present=True).count()
    
    # Weekly attendance rate
    week_attendance = StudentAttendance.objects.filter(date__gte=week_ago, date__lte=today)
    week_total = week_attendance.count()
    week_present = week_attendance.filter(is_present=True).count()
    attendance_rate = round((week_present / week_total * 100) if week_total > 0 else 0, 1)
    
    # Recent attendance records
    recent_attendance = StudentAttendance.objects.select_related('student').order_by('-date', '-id')[:5]
    
    # Weekly summary
    weekly_summary = []
    for i in range(7):
        day = today - timedelta(days=i)
        day_records = StudentAttendance.objects.filter(date=day)
        present_count = day_records.filter(is_present=True).count()
        absent_count = day_records.filter(is_present=False).count()
        total_count = present_count + absent_count
        rate = round((present_count / total_count * 100) if total_count > 0 else 0, 1)
        
        weekly_summary.append({
            'date': day,
            'present': present_count,
            'absent': absent_count,
            'rate': rate
        })
    
    context = {
        'total_students': total_students,
        'total_farmers': total_farmers,
        'today_present': today_present,
        'attendance_rate': attendance_rate,
        'recent_attendance': recent_attendance,
        'weekly_summary': weekly_summary,
    }
    return render(request, 'attendance/dashboard.html', context)


def export_attendance_csv(request):
    """Export attendance records to CSV."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_records.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Student Name', 'Class', 'School', 'Date', 'Status'])
    
    # Get filtered records if any
    attendance_records = StudentAttendance.objects.select_related('student').all()
    
    date_filter = request.GET.get('date', '')
    if date_filter:
        try:
            filter_date = _date.fromisoformat(date_filter)
            attendance_records = attendance_records.filter(date=filter_date)
        except Exception:
            pass
    
    status_filter = request.GET.get('status', '')
    if status_filter == 'present':
        attendance_records = attendance_records.filter(is_present=True)
    elif status_filter == 'absent':
        attendance_records = attendance_records.filter(is_present=False)
    
    attendance_records = attendance_records.order_by('-date', 'student__name')
    
    for record in attendance_records:
        writer.writerow([
            record.student.name,
            record.student.class_name,
            record.student.school,
            record.date.strftime('%Y-%m-%d'),
            'Present' if record.is_present else 'Absent'
        ])
    
    return response


def bulk_mark_attendance(request):
    """Bulk mark all students as present or absent for a date."""
    if request.method == 'POST':
        date_str = request.POST.get('date')
        action = request.POST.get('action')  # 'present' or 'absent'
        
        try:
            date = _date.fromisoformat(date_str) if date_str else timezone.now().date()
        except Exception:
            date = timezone.now().date()
        
        is_present = (action == 'present')
        students = Student.objects.all()
        count = 0
        
        for student in students:
            obj, created = StudentAttendance.objects.get_or_create(
                date=date,
                student=student,
                defaults={'is_present': is_present}
            )
            if not created and obj.is_present != is_present:
                obj.is_present = is_present
                obj.save()
            count += 1
        
        status_text = 'present' if is_present else 'absent'
        messages.success(request, f'Marked {count} students as {status_text} for {date}.')
        return redirect('mark_attendance')
    
    return redirect('mark_attendance')


def farmer_list_json(request):
    """Return farmers list as JSON."""
    farmers = Farmer.objects.all().values(
        'id', 'name', 'phone', 'farm',
        'gender', 'employment_type', 'age', 'location'
    )
    return JsonResponse(list(farmers), safe=False)


def student_list_json(request):
    """Return students list as JSON."""
    students = Student.objects.all().values(
        'id', 'name', 'class_name', 'age',
        'gender', 'school'
    )
    return JsonResponse(list(students), safe=False)


def view_farmer(request, pk):
    """View farmer details."""
    farmer = get_object_or_404(Farmer, pk=pk)
    return render(request, 'attendance/view_farmer.html', {'farmer': farmer})


def view_student(request, pk):
    """View student details."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'attendance/view_student.html', {'student': student})
