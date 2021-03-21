from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custom_permission import MyPermission
# Create your views here.
class MyView(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class  =StudentSerializer
    authentication_classes  = [SessionAuthentication]
    permission_classes=[MyPermission]
