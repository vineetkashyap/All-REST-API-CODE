from app import  views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('stu',views.MyViewSet,basename='stu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
