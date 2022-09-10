from rest_framework.routers import DefaultRouter
from .views import (
    ProductRatingViewSet,
    ProductsViewSet
)
from django.urls import (
    path,
    include
)


router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'product-rating', ProductRatingViewSet, basename='product-rating')

products_urls = [
    path('', include(router.urls))
]