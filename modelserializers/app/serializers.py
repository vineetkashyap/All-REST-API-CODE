from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Merta:
        model = Student
        fields = '__all__'
        # fields = ['id','name','roll','city']
        # exclude  =['roll']