from django.contrib import admin

# Register your models here.
from aboutpage.models import aboutpage
class AboutAdmin(admin.ModelAdmin):
    list_display=('aboutpage_title','aboutpage_img','aboutpage_desc','aboutpage_uploading')

admin.site.register(aboutpage,AboutAdmin)

