from django.db import models
import os
from django.contrib.auth.models import  User

# Create your models here.
def get_upload_path(instance, filename):
    return os.path.join('docs', instance.owner.username, filename)

class Document1(models.Model):
    owner = models.ForeignKey(User)
    docfile = models.FileField(upload_to=get_upload_path)
    
               
class UserProfile(models.Model):
    GENDER = (
            ('m', 'Male'),
            ('f', 'Female'),
            )
    
    gender = models.CharField(max_length=1, choices=GENDER, default='m')
    user = models.ForeignKey(User)
    

