from rest_framework.routers import DefaultRouter
from .views import (
    ProductsViewSet, 
    ProductRating
)
from django.urls import (
    path,
    include
)


router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'product-reviews', ProductRating, basename='product-reviews')

products_urls = [
    path('', include(router.urls)),
]