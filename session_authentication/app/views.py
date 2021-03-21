from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
class MyView(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class =StudentSerializer
    authentication_classes=[SessionAuthentication]

    permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    permission_classes=[DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    permission_classes=[IsAuthenticatedOrReadOnly]
