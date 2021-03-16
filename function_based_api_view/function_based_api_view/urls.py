from app import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/',views.student_data,name='stu'),
]
