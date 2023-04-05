from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializers, UserSerializers, ArticleSerializers, AuthorSerializers
from .models import Course
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import permissions
from django.views.generic import ListView
from .models import Article
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsSuperuserOrStaffReadOnly, IsStaffOrReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Course.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     return queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]


class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetails(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [permissions.IsAdminUser, IsAuthorOrReadOnly]


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # filter with status and author id
    filterset_fields = ['status', 'author']

    search_fields = ['title', 'content', 'author__username', 'author__first_name', 'author__last_name']

    ordering_fields = ['publish', 'status']
    # default ordering
    ordering = ['-publish']

    # filter with status and username ---dosent work
    # filterset_fields = ['status', 'author__username']
    # filterset_fields = {
    #     'status': ['exact'],
    #     'author': ['exact', 'username']
    # }

    # a bad way for filter (Filtering against query parameters)
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         # queryset = queryset.filter(author=author)
    #         queryset = queryset.filter(author__username=author)
    #     return queryset


# این ویوو باید در اپلیکیشن جداگانه ای مثلا اپ blog ایجاد شود
# به همره مدل و url باید منتقل شوند
class ArticleListView(ListView):
    template_name = './blog/article_list.html'

    def get_queryset(self):
        return Article.objects.all()


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperuserOrStaffReadOnly,)


class UserListView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperuserOrStaffReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class AuthorRetrieveView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    # queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializers

    # def get_queryset(self, **kwargs):
    #     user = get_user_model().objects.filter(id=kwargs)
    #     return user
