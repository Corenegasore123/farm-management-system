from django.db import models

# Create your models here.

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    farm = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    phone = models.CharField(max_length=20, blank=True, null=True)
    EMPLOYMENT_CHOICES = [
        ('contract', 'Contract'),
        ('casual', 'Casual'),
    ]
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'farmer'
        ordering = ['name']


    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [      
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    school = models.CharField(max_length=150)

    class Meta:
        db_table = 'student'
        ordering = ['name']

    def __str__(self):
        return self.name

class Attendance(models.Model):
    date = models.DateField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.farmer.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"


    class Meta:
        db_table = 'attendance'
        ordering = ['-date']


class StudentAttendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    class Meta:
        db_table = 'student_attendance'
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(fields=['date', 'student'], name='uniq_student_date')
        ]

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
