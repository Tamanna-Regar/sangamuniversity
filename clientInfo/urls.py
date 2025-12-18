from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_page, name='about'), # HTML Page
    path('api/clients/', views.get_clients, name='get_clients'), # API GET
    path('api/add/', views.add_client, name='add_client'), # API POST
]