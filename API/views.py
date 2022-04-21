from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializers, UserSerializers
from .models import Course
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]

