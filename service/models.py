from django.db import models

# Create your models here.
class Service(models.Model):
    service_title= models.CharField(max_length=500)
    service_img = models.CharField(max_length=500)
    service_desc=models.TextField()
    service_uploading=models.FileField(upload_to="Service", max_length=500,null=True,default=None)

