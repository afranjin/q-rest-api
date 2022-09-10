from django.contrib import admin
from django.urls import (
    path,
    include
)
from .views import (
    LoginView,
    LogoutView
)
from products.urls import products_urls


auth_urls = [
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view()),
]

api_urls = [
    path('', include(auth_urls)),
    path('', include(products_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]
