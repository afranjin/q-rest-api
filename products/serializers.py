from rest_framework import serializers
from .models import (
    Product,
    ProductRating
)


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'rating',
        )


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = '__all__'