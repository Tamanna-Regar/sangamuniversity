from django.db import models
class Category(models.Model):
    Catname=models.CharField(max_length=250)
    def __str__(self):
        return self.Catname
    
class Post(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    datetime_post = models.DateTimeField(default=None)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


