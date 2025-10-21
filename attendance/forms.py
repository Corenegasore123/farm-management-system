from django import forms
from django.forms import widgets
from .models import Farmer, Student  

class FarmerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employment_type'].required = True
        self.fields['employment_type'].choices = [
            ('', 'Select employment type')
        ] + list(Farmer.EMPLOYMENT_CHOICES)

    class Meta:
        model = Farmer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Name',
                'id': 'name',
            }),
            'farm': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Farm Name',
                'id': 'farm',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Age',
                'id': 'age',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Location',
                'id': 'location',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2',
                'placeholder': 'Phone (optional)',
                'id': 'phone',
            }),
            'employment_type': forms.Select(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'id': 'employment_type',
                'required': 'required',
            }),
            'gender': forms.RadioSelect(choices=Farmer.GENDER_CHOICES, attrs={
                'class': 'form-check-input text-accent focus:ring-accent',
            }),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Name',
                'id': 'name',
            }),
            'class_name': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Class',
                'id': 'class_name',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'Age',
                'id': 'age',
            }),
            'school': forms.TextInput(attrs={
                'class': 'form-control block w-full rounded-xl border border-slate-200 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-accent-soft focus:border-accent',
                'placeholder': 'School',
                'id': 'school',
            }),
            'gender': forms.RadioSelect(choices=Student.GENDER_CHOICES, attrs={
                'class': 'form-check-input text-accent focus:ring-accent',
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
            
