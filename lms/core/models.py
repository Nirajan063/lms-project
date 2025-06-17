from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
SUBJECT= [
    ('BCT001', 'Software Engineering'),
    ('BCT002', 'System Analysis'),
    ('BCT003', 'Operating Systems'),
    ('BCT004', 'Instrumentation')
]

class Student(models.Model):
    SEMESTER= [
        ('SEM_ONE', 'Semester one'),
        ('SEM_TWO', 'Semester two'),
        ('SEM_THREE', 'Semester three'),
        ('SEM_FOUR', 'Semester four'),
        ('SEM_FIVE', 'Semester five'),
        ('SEM_SIX', 'Semester six'),
        ('SEM_SEVEN', 'Semester seven'),
        ('SEM_EIGHT', 'Semester eight')
    ]
    full_name= models.CharField(max_length=200, null=False,blank=False,verbose_name="student full name")
    email = models.CharField(max_length=100, unique=True, null=False,blank=False, verbose_name="student email")
    semester = models.CharField(max_length=10,choices=SEMESTER, default='N/A', null=True,blank=True)
    phone_no= models.IntegerField(null=False,blank=False)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        ordering = ['-full_name']

    def __str__(self):
        return self.full_name
    
class Teacher(models.Model):
    DEPARTMENT=[
        ('BCA', 'Bachelor in computer application'),
        ('BCT', 'Bachelor in electronics and information'),
        ('BCE', 'Bachelor in civil Engineering')
    ]

    full_name= models.CharField(max_length=200, null=False,blank=False,verbose_name="teacher full name")
    email = models.CharField(max_length=100, unique=True, null=False,blank=False, verbose_name="Teacher email")
    department= models.CharField(max_length=5,choices=DEPARTMENT, default='N/A', null=True,blank=True)
    phone_no= models.IntegerField(null=False,blank=False)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name='teacher'
        verbose_name_plural= 'teachers'
        ordering= ['-full_name']

    def __str__(self):
        return self.full_name
    
class Assignment(models.Model):
    title= models.CharField(max_length=100,null=False,blank=False,verbose_name='Assignmenyt Title')
    start_date= models.DateField(default='Start date', blank=False, null=False,verbose_name='start date')
    end_date= models.DateField(default='End Date', blank=False, null=False,verbose_name='End Date')
    question_file= models.FileField(upload_to='assignments/questions/', null= True,blank= True,verbose_name='Assignment question files')
    question= models.TextField(null=True,blank=True, verbose_name='assignment questions')
    remark= models.CharField(max_length=100, null=False,blank=False,verbose_name='assignment Details')
    full_mark = models.FloatField(blank=False, null=False)
    teacher =models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='uploaded by' )
    subject= models.CharField(max_length=20, choices=SUBJECT,default='N/A', verbose_name='Subject')

    class Meta:
        verbose_name ='Assignment '
        verbose_name_plural= 'Assignments'
        ordering= ['-title']
    def __str__(self):
        return self.title
    
class Material(models.Model):
    MATERIAL_CATEGORY=[
        ('SLIDE', 'Chapter Slide'),
        ('TEXT_BOOK', 'A text book'),
        ('REFERENCE_BOOK','A Reference book'),
        ('OLD_QUESTION','Previous board Exam question'),
        ('AUDIO_BOOK', 'An audio book')
    ]
        
    title = models.CharField(max_length=100,null=False,blank=False,verbose_name='material')
    category = models.CharField(max_length=20, null=False,blank=False, verbose_name='category')
    description= models.CharField(max_length=200, null=False,blank=False,verbose_name='Material description')
    subject= models.CharField(max_length=20, choices=SUBJECT, default='N/A', verbose_name='subject')
    files = models.FileField(upload_to='material/', null=False,blank=False,verbose_name='Select file')
    upload_date =models.DateTimeField(default=datetime.now(), verbose_name='upload Date')
    teacher= models.ForeignKey(Teacher,on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Material '
        verbose_name_plural= 'MAterials'
        ordering= ['-title']
    def __str__(self):
        return self.title