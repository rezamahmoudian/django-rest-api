from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializers, UserSerializers, ArticleSerializers
from .models import Course
from django.contrib.auth.models import User
from rest_framework import permissions
from django.views.generic import ListView
from .models import Article
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsSuperuserOrStaffReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]


class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetails(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [permissions.IsAdminUser, IsAuthorOrReadOnly]


# این ویوو باید در اپلیکیشن جداگانه ای مثلا اپ blog ایجاد شود
# به همره مدل و url باید منتقل شوند
class ArticleListView(ListView):
    template_name = './blog/article_list.html'

    def get_queryset(self):
        return Article.objects.all()


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperuserOrStaffReadOnly,)


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperuserOrStaffReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)
