from django import forms
from core.models import Teacher, Assignment

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        } 

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment  # Assuming Assignment is a model related to Teacher
        fields = ['title', 'start_date', 'end_date', 'question_file', 'question', 'full_mark', 'teacher', 'assignment_subject', 'remark']
        widgets = {
            'strat_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }