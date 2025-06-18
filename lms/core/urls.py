from django.urls import path
from core.views import (HomePageView,
                        TeacherCreateView, 
                        TeacherListView,
                        TeacherUpdateView,
                        TeacherDeleteView ,
                        TeacherDetailView)

urlpatterns = [
    #path('', views.home, name='home') -function base views loading
    path('', HomePageView.as_view(), name='home'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create'),
    path('teacher/edit/<int:pk>/', TeacherUpdateView.as_view(), name='teacher.edit'),
    path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher.delete'),
    path('teacher/detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher.detail'),
]
