from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import *
from .serializer import CarSerializer

# Create your views here.

class CarsDisplayView(APIView):

    permission_classes = [AllowAny] 

    def get(self,request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars,context={"request" : request}, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)