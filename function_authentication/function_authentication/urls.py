
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/',views.index,name='stu'),
    path('stu/<int:pk>/',views.index,name='stu'),
    path('auth/',include('rest_framework.urls',namespace='student')),

]
