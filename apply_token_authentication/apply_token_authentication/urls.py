
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('stu',views.MyView,basename='stu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
