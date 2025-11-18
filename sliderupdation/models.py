from django.db import models

# Create your models here.
class SliderUpdate(models.Model):
    slider_title= models.CharField(max_length=500)
    slider_img = models.CharField(max_length=500)
    slider_desc=models.TextField()
    slider_uploading=models.FileField(upload_to="Sliderupdation", max_length=500,null=True,default=None)

