from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class  MyView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated ]