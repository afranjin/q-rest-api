import pytest
from products.serializers import (
    ProductSerializer,
    ProductRatingSerializer
)

@pytest.mark.django_db
def test_product_serializer(sample_q_product):
    serializer = ProductSerializer(sample_q_product)

    assert 'id' in serializer.data
    assert serializer.data.get('id') == sample_q_product.id
    assert 'name' in serializer.data
    assert serializer.data.get('name') == sample_q_product.name
    assert 'price' in serializer.data
    assert serializer.data.get('price') == sample_q_product.price
    assert 'rating' in serializer.data
    assert serializer.data.get('rating') == sample_q_product.rating


@pytest.mark.django_db
def test_product_rating_serializer(sample_q_product_rating):
    serializer = ProductRatingSerializer(sample_q_product_rating)

    assert 'id' in serializer.data
    assert serializer.data.get('id') == sample_q_product_rating.id
    assert 'product' in serializer.data
    assert serializer.data.get('product') == sample_q_product_rating.product.id
    assert 'user' in serializer.data
    assert serializer.data.get('user') == sample_q_product_rating.user.id
    assert 'product_rating' in serializer.data
    assert serializer.data.get('product_rating') == sample_q_product_rating.product_rating