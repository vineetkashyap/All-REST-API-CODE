
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from app.auth import CustomAuthToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/',CustomAuthToken.as_view())
]
