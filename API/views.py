from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializers
from .models import Course


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
