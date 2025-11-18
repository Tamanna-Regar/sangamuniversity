from django.db import models
from datetime import datetime

# Create your models here.
class Contactform(models.Model):
    Username=models.CharField(max_length=500)
    Usersubject=models.CharField(max_length=500)
    UserEmail=models.CharField(max_length=500)
    Usermessage=models.TextField()
    submitdate=models.DateTimeField(default=datetime.now)



