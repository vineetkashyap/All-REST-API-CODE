from django.shortcuts import render
from .models import Student 
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

class MyList(GenericAPIView,ListModelMixin):
    queryset =Student.objects.all()
    serializer_class =StudentSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class MyCreate(GenericAPIView,CreateModelMixin):
    queryset =Student.objects.all()
    serializer_class =StudentSerializers
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class MyUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class MyDelete(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 

class MyRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
