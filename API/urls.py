from django.urls import path, include, re_path
from rest_framework import routers
from .views import CourseViewSet, UserViewSet
from rest_framework_simplejwt import views as jwt_views
from .views import ArticleListView, ArticleListCreateAPIView, ArticleDetails, UserListView,\
    UserDetail, ArticleListApiView, AuthorRetrieveView  #,RevokeToken
from dj_rest_auth.views import PasswordResetConfirmView
# drf yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('articles', CourseViewSet, basename='course')
router.register('user', UserViewSet, basename='user')

app_name = 'api'

schema_view = get_schema_view(
   openapi.Info(
      title="My Project API",
      default_version='v1',
      description="all endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="reza@site.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('', ArticleListView.as_view(), name='home'),
    path('articles/', ArticleListApiView.as_view(), name='articles'),
    path('list/', ArticleListCreateAPIView.as_view(), name='list'),
    path('<int:pk>', ArticleDetails.as_view(), name='article-detail'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('author/<int:pk>', AuthorRetrieveView.as_view(), name='author-detail'),
    # path('api-token-auth/', views.obtain_auth_token),
    # path('revoke-token/', RevokeToken.as_view(), name="revoke-token"),
    path('password/reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # drf yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
