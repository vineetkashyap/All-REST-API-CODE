from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentSAdmin(admin.ModelAdmin):
    lsit_display=['id','name','roll','city']
