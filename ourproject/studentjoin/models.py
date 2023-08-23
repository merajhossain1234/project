from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    batch = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    registration_number=models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=15)
    room_no=models.IntegerField(null=True, blank=True)
    border_no = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField()
    is_member = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
