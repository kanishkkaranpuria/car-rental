from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import *
from .serializer import BookingSerializer

# Create your views here.

class CreateBookingView(APIView):

    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = BookingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"data saved"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
