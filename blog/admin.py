from django.contrib import admin

# Register your models here.
from blog.models import Category,Post

class AdminCategory(admin.ModelAdmin):
  list_display=('id', 'Catname')
class AdminPost(admin.ModelAdmin):
  list_display=('id','title','content','datetime_post','category_name')

admin.site.register(Category,AdminCategory)
admin.site.register(Post,AdminPost)
