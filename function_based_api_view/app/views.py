from django.shortcuts import render
from rest_framework.decorators import api_view
from  .models import Student
from rest_framework.response import Response
from .serializers import StudentSerializers
from rest_framework import status
# Create your views here.
@api_view(['POST','GET','PUT'])
def student_data(request):
    if request.method =='GET':
        id = request.data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =Student.objects.all()
            serializer = StudentSerializers(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data is inserted'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializers =StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data updated'}
            return Response(res,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res  ={'msg':'data deleted'}
        return Response(res,status=status.HTTP_202_ACCEPTED)











