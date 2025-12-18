from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ClientInfo
from .serializers import ClientInfoSerializer

# HTML Page ke liye
def about_page(request):
    return render(request, 'about.html')

# API: Sabhi clients dekhne ke liye
@api_view(['GET'])
def get_clients(request):
    clients = ClientInfo.objects.all()
    serializer = ClientInfoSerializer(clients, many=True)
    return Response(serializer.data)

# API: Naya client add karne ke liye
@api_view(['POST'])
def add_client(request):
    serializer = ClientInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Client added!", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)