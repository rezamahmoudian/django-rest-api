from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('', CourseViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
