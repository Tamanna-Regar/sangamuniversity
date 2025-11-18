from django.contrib import admin
from contctdetail.models import Contactform
class ContctAdmin(admin.ModelAdmin):
    list_display=('Username','UserEmail','Usersubject','Usermessage')
    
admin.site.register(Contactform,ContctAdmin)

