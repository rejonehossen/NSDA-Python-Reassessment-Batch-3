from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    full_name= models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='static/image')
    
    skills=models.CharField(max_length=100, null=True)
    
    work_experience=models.CharField(max_length=100, null=True)
    
    
    education=models.CharField(max_length=150, null=True)
    
    phone= models.CharField(max_length=50, null=True)
    address=models.CharField(max_length=100, null=True)
    city=models.CharField(max_length=100, null=True)
    country=models.CharField(max_length=100, null=True)
    
    about= models.TextField(null=True, blank=True)