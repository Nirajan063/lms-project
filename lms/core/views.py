from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from core.models import Teacher, Student, Assignment

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'
    paginate_by = 5 

class TeacherCreateView(TemplateView):
    model= Teacher
    fields=['full_name', 'email', 'department', 'phone_no', 'user']
    template_name = 'teachers/teacher_form.html'
    success_url = 'teacher.index'
