from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MyViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        return Response(serializers.data)
    def retrieve(self,request,pk=None):
        id =pk
        if id is not  None:
            stu = Student.objects.get(id=id)
            serializers= StudentSerializers(stu)
            return Response(serializers.data)
    def  create(self,request):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            res ={'msg':'data inserted successfully'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def  partial_update(self,request,pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer= StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res ={"msg":"data updated successfully"}
            return Response(res,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def  update(self,request,pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer= StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res ={"msg":"data updated successfully"}
            return Response(res,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":"data deleted"}
        return Response(res,status=status.HTTP_200_OK)
    
        




