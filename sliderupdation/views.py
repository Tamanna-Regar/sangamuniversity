from django.shortcuts import render
from sliderupdation.models import SliderUpdate

def Home_Page(request):
    sliderUpdateData=SliderUpdate.objects.all()


    Data={
        'sliderUpdateData':sliderUpdateData,

    }

    return render(request,"index.html",Data)
 
