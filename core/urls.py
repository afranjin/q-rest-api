from django.contrib import admin
from django.urls import (
    path,
    include,
    re_path
)
from .views import (
    LoginView,
    LogoutView
)
from products.urls import products_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Q-drf-api",
      default_version='v1',
      description="Q api",
      terms_of_service=""
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urls = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]


auth_urls = [
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view()),
]

api_urls = [
    path('', include(auth_urls)),
    path('', include(products_urls))
]

urlpatterns = [
    path('', include(swagger_urls)),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]
