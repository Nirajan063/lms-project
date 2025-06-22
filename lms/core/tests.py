from django.test import TestCase
from core.models import Teacher 
from django.contrib.auth.models import User
# Create your tests here.

class TeacherModelTest(TestCase):

    def test_teacher_model_creation(self):
        teacher = Teacher.objects.create(
            full_name="John cens",
            email="johnsinha23@gmail.com",
            department="BEI",
            phone_no="98000000",
            join_date= "2025-02-04",
            #user= User.objects.get(id=9)  #Assuming user with id 9 exists
            #assuming user not exists so creating new user
            user= User.objects.create_user(username="testuser", password="nepal123")
        )
        try:
            #case one: user exists
            print("case 0ne:user exist with same user name")
            teacher.full_clean()  # Validate the model instance
            self.assertEqual(teacher.full_name, "John cens")
            self.assertEqual(teacher.email, "johnsinha23@gmail.com")
            self.assertEqual(teacher.department, "BEI")
            self.assertEqual(teacher.phone_no, "98000000")    
            self.assertEqual(teacher.join_date, "2025-02-04")
            self.assertEqual(teacher.user, User.objects.get(username="testuser" ))
        except Exception as e:
            print("eroor:", e)

        try:
            #case two: user with different username 
            print("case 0ne:user exist with same user name")
            teacher.full_clean()  # Validate the model instance
            self.assertEqual(teacher.full_name, "John cens")
            self.assertEqual(teacher.email, "johnsinha23@gmail.com")
            self.assertEqual(teacher.department, "BEI")
            self.assertEqual(teacher.phone_no, "98000000")    
            self.assertEqual(teacher.join_date, "2025-02-04")
            self.assertEqual(teacher.user, User.objects.get(username="" )) #different user
        except Exception as e:
            print("error:", e)
            print("error: user must be same for teacher")

        try:
            #case three: user with different username 
            print("case three:user exist with same user name")
            teacher.full_clean()  # Validate the model instance
            self.assertEqual(teacher.full_name, "John cens")
            self.assertEqual(teacher.email, "johnsinha23@gmail.com")
            self.assertEqual(teacher.department, "BEI")
            self.assertEqual(teacher.phone_no, "9800000000")    
            self.assertEqual(teacher.join_date, "2025-02-04")
            self.assertEqual(teacher.user, User.objects.get(username="" )) #different user
        except Exception as e:
            print("eroor:", e)
            print("error: Required phone no length is 9.")
        
                             