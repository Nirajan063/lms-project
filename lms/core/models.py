from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    class meta:
        Verbose_name = "student"
        Verbose_name_plural = "students"
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

    class meta:
        verbose_name='teacher'
        verbose_name_plural= 'teacher'
        ordering= ['-full_name']

    def __str__(self):
        return self.full_name
    
    class Assignment(models.Model):
        title= models.CharField(max_length=100,null=False,blank=False,verbose_name='Assignmenyt Title')
        start_date= models.DateField(default='Start date', blank=False, null=False,verbose_name='start date')
        end_date= models.DateField(default='End Date', blank=False, null=False,verbose_name='End Date')
        question_file= models.models.FileField(_ upload_to='assignments/questions/', null= True,blank= True,verbose_name='Assignment question files')
        question= models.TextField(null=True,blank=True, verbose_name='assignment questions')
        remark= models.CharField(max_length=100, null=False,blank=False,verbose_name='assignment Details')
        full_mark = models.FloatField(blank=False, null=False)
        teacher =models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='uploaded by' )
        class meta:
            verbose_name ='Assignment '
            verbose_name_plural= 'Assignment'
            ordering= ['due_Date']
        def __str__(self):
            return self.title