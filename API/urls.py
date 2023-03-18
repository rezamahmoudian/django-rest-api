from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, UserViewSet
from rest_framework_simplejwt import views as jwt_views
from .views import ArticleListView, ArticleListCreateAPIView, ArticleDetails, UserListView, UserDetail  #,RevokeToken
from dj_rest_auth.views import PasswordResetConfirmView

router = routers.DefaultRouter()
router.register('', CourseViewSet)
router.register('user', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('', ArticleListView.as_view(), name='home'),
    path('list/', ArticleListCreateAPIView.as_view(), name='list'),
    path('<int:pk>', ArticleDetails.as_view(), name='article-detail'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('api-token-auth/', views.obtain_auth_token),
    # path('revoke-token/', RevokeToken.as_view(), name="revoke-token"),
    path('password/reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
