from django.http import HttpResponse
from django.shortcuts import render
from contctdetail.models import Contactform
from sliderupdation.models import SliderUpdate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import requests


def Home_Page(request):
   data=SliderUpdate.objects.all()
   alldata={
      'data':data
   }
   return render(request,"index.html",alldata)
def about_page(request):
   return render(request,"about.html")

def service_page(request):
   return render(request,"service.html")

def booking_page(request):
   return render(request,"booking.html")

def login_page(request):
   return render(request,"login.html")


def contact_page(request):
   msg=""
   if request.method=='POST':
      Username=request.POST.get('Username')
      UserEmail=request.POST.get('UserEmail')
      Usersubject=request.POST.get('Usersubject')
      Usermessage=request.POST.get('Usermessage')
      allData=Contactform(Username=Username,UserEmail=UserEmail,Usersubject=Usersubject,Usermessage=Usermessage)
      allData.save()
      msg='form Submitted!'
      #Render HTML template
      html_contact=render_to_string('email_template.html',{
          'Username':Username,
          'UserEmail':UserEmail,
          'Usersubject': Usersubject,
          'Usermessage': Usermessage,
      })
      #email content
      send_mail(
                  subject="Testing mail",
                  message="Hello Sangam University",
                  from_email="Tamannaregar2@gmail.com",
                  recipient_list=["payalkanwar4433@gmail.com"],
                  fail_silently=False,
      )
      #Send admin notification (plain text)
      admin_subject = f"New Contact Form Submission from {Username}"
      admin_message = (
      f"Name: {Username}\n"
      f"Email: {UserEmail}\n"
      f"Subject': {Usersubject}\n"
      f"Message': {Usermessage}\n"
      )
      admin_email = EmailMultiAlternatives(
      subject=admin_subject,
      body=admin_message,
      from_email="v9d2412@gmail.com",
      to=["tamannaregar2@gmail.com"],
      )
      admin_email.send(fail_silently=False)

   return render(request,'contact.html',{'msg':msg})


import requests
from django.shortcuts import render
def weatherData(request):
      # API URL 
      api_url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current_weather=true"

      # Fetch the data from the API
      response = requests.get(api_url)
      if response.status_code == 200:
         weather_data = response.json() # Parse the JSON response
         weather = weather_data.get('current_weather',{}) # Extract the data&key
      else:
         weather = {} # Handle the case where the API is notreachable
      # Pass the data to the template
      return render(request,'weather.html', {'weather':weather})


