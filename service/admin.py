from django.contrib import admin

# Register your models here.
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title','service_img','service_desc','service_uploading')

admin.site.register(Service,ServiceAdmin)
