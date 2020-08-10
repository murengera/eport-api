from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import  get_user_model
User=get_user_model()
from .models import  Program
class BlogPostAPITestCase(APITestCase):
    def SetUp(self):
        user_obj=User(username='testcfeuser',email='test@test.com')
        user_obj.set_password("dalton")
        user_obj.save()
        university=Program.objects.create(user=user_obj,
                                          program='postgrate',
                                          university="UR")


    def test_single_user(self):
         user_count=User.objects.count()
         self.assertEqual(user_count,1)




