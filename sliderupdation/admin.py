from django.contrib import admin

# Register your models here.
from sliderupdation.models import SliderUpdate
class SliderAdmin(admin.ModelAdmin):
    list_display=('slider_title','slider_img','slider_desc','slider_uploading')

admin.site.register(SliderUpdate,SliderAdmin)
