from rest_framework import (
    viewsets,
    status,
    filters
)
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)
from django.db.models.query import QuerySet
from core.contrib.unique_none import get_unique_or_none
from .models import (
    Product,
)
from django.db.models.functions import Lower
from .serializers import (
    ProductSerializer,
)
from .product_pagination import ProductPagination


class ProductsViewSet(viewsets.ModelViewSet):
    """
    Viewing, creating, editing and delete Product instances
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    search_fields = (
        'name',
        'price',
        'rating',
        'updated_at',
    )

    ordering_fields = (
        'name',
        'price',
        'rating',
        'updated_at',
    )

    ordering = ('name', )

    def not_found(self):
        return Response(
            {'error': 'Product not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    def get_object(self):
        return get_unique_or_none(Product, id=self.kwargs.get('pk'))

    def get_ordered_queryset(self, qs, initial_order):
        """This will support insensitive ordering.
        Args:
            qs: qs of Product instance
            initial_order: initial ordering if query_params not provided 
        Returns:
            QuerySet: sorted QuerySet
        """
        order_by = self.request.query_params.get('ordering')

        if not order_by:
            order_by = initial_order

        if order_by.startswith('-'):
            return sorted(qs.order_by(
                Lower(order_by[1:])),
                key=lambda x: x.__dict__[order_by[1:]].lower(),
                reverse=True
            )
        return qs.order_by(Lower(order_by))

    def list(self, request):
        """Return list of all products as paginatied response or normal one"""
        try:
            queryset = self.get_ordered_queryset(
                self.filter_queryset(self.get_queryset()),
                'name'
            )

            page = self.paginate_queryset(queryset)
            if page is not None and request.query_params.get('page', None):
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': e},
                status=status.HTTP_400_BAD_REQUEST
            )
