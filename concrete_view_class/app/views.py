from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

class MyList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
class MyList1(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
class MyList2(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
class MyList3(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
class MyList4(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers

