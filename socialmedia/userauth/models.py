from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio=models.TextField(blank=True ,default='')
    profileimg=models.ImageField(upload_to='profile_images',default='blank_profile_pic.png')
    location=models.CharField(max_length=100 ,blank=True,default='')
    
    def __str__(self):
        return self.user.username
    
    

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile=models.CharField(max_length=10)
    address=models.TextField()

    def __str__(self):
        return self.name