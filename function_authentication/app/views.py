from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import permission_classes,authentication_classes,api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST','DELETE','PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def index(request,pk=None):
    if request.method=='GET':
        stu = Student.objects.all()
        serializer= StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data inserted successfully'}
            return Response(res)
        return Response(serializer.errors)
    if request.method=='PUT':
        id=pk
        stu = Student.objects.get(id=id)
        serializer= StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            red = {'msg':'data updated successfully'}
            return Response(red)
        return Response(serializer.errors)
    if request.method=='DELETE':
        stu =Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'data deleted successfully'})




