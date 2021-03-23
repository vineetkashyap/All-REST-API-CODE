from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MyView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    authentication_classes  =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
