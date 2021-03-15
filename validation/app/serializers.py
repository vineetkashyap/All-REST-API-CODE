from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    # id  = serializers.IntegerField()
    def start_with_s(value):
        if value[0].lower() != 's':
            raise serializers.ValidationError("name should be start with s")
    name = serializers.CharField(max_length=100,validators=[start_with_s])
    roll  =serializers.IntegerField()
    city  =serializers.CharField(max_length=100)
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
########field level validation##################
    def validate_roll(self, value):
        if value >200:
            raise serializers.ValidationError("seat full")
        return value
# ###########object level validation###############
    def validate(self, value):
        nm = value.get('name')
        ct =value.get('city')
        if nm.lower() != 'vineet':
            raise serializers.ValidationError("name must be vineet ")
        return value

