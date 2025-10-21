

from django import forms
from django.forms import widgets
from .models import Farmer, Student  
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'id': 'name',
            }),
            'farm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Farm',
                'id': 'farm',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age',
                'id': 'age',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location',
                'id': 'location',
            }),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'id': 'name',
            }),
            'class_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Class',
                'id': 'class_name',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age',
                'id': 'age',
            }),
            'school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'School',
                'id': 'school',
            }),
        }

# class AttendanceForm(forms.ModelForm):
#     class Meta:
#         model = Attendance
#         fields = '__all__'

#         widgets = {
            
#             'date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Date',
#                 'id': 'date',
#             }),
#             'farmer': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Farmer',
#                 'id': 'farmer',
#             }),
#             'is_present': forms.CheckboxInput(attrs={
#                 'class': 'form-check-input',
#                 'id': 'is_present',
#             }),
#         }
            
