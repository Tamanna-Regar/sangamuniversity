from django.db import models

# Create your models here.
class aboutpage(models.Model):
    aboutpage_title= models.CharField(max_length=500)
    aboutpage_img = models.CharField(max_length=500)
    aboutpage_desc=models.TextField()
    aboutpage_uploading=models.FileField(upload_to="aboutpage", max_length=500,null=True,default=None)


