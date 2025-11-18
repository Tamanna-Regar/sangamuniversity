from django.shortcuts import render
from  django.http import HttpResponse
from  django.shortcuts import render
from contctdetail.models import Contactform

def Home_Page(request):
   return render(request,"index.html")
def about_page(request):
   return render(request,'about.html')
def contact_page(request):
   msg=""
   if request.method=='POST':
      Username=request.POST.get('Username')
      UserEmail=request.POST.get('UserEmail')
      Usersubject=request.POST.get('Usersubject')
      Usermessage=request.POST.get('Usermessage')
      allData=Contactform(Username=Username,UserEmail=UserEmail,Usersubject=Usersubject,Usermessage=Usermessage)
      allData.save()
      msg="form Submitted!"
   return render(request,"contact.html",{'msg':msg})

