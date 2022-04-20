from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet


router = routers.DefaultRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]