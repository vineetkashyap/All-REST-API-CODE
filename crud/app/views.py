from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io
from rest_framework.parsers import JSONParser
# Create your views here.

def index(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data,many=True)
    json_data  = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data,content_type="application/json")
@method_decorator(csrf_exempt,name='dispatch')
class Index(View):
    def get(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is None:
            stu  =Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)
        else  :
            stu  = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
          
    def post(self,request):
        json_data= request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializers  =StudentSerializer(data = python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data has been inserted'}
            json_data  = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data =JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')

    def  put(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id  = python_data.get('id')
        stu = Student.objects.get(id =id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def delete(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':"'data deleted"}
        return JsonResponse(res,safe=False)


            
    
