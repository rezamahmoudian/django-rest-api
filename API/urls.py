from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, UserViewSet
from rest_framework_simplejwt import views as jwt_views
from .views import ArticleListView, ArticleListCreateAPIView, ArticleDetails, UserListView, UserDetail


router = routers.DefaultRouter()
router.register('', CourseViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', ArticleListView.as_view(), name='home'),
    path('list/', ArticleListCreateAPIView.as_view(), name='list'),
    path('<int:pk>', ArticleDetails.as_view(), name='article-detail'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
