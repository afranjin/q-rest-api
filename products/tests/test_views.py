import pytest
from rest_framework.test import APIRequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from products.views import (
    ProductsViewSet,
    ProductRatingViewSet
)


# Product
@pytest.mark.django_db
def test_product_view_set_list(sample_q_product):
    """Test products ViewSet list part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductsViewSet.as_view({'get': 'list'})
    request = factory.get('products/')
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_view_set_retrieve(sample_q_product):
    """Test product ViewSet retrieve part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductsViewSet.as_view({'get': 'retrieve'})
    request = factory.get('products/')
    response = view(request, pk=sample_q_product.id)

    assert response.status_code == 200



@pytest.mark.django_db
def test_product_view_set_create():
    """Test product ViewSet create part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductsViewSet.as_view({'post': 'create'})
    request = factory.post('products/', {
        'id': '',
        'name': 'SampleProduct',
        'price': '1.00',
        'rating': 0.0
    }, format='json')
    response = view(request)

    assert response.status_code == 201


@pytest.mark.django_db
def test_product_view_set_update(sample_q_product):
    """Test product ViewSet update part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductsViewSet.as_view({'put': 'update'})
    request = factory.put('products/', {
        'id': sample_q_product.id,
        'name': sample_q_product.name,
        'price': sample_q_product.price,
        'rating': sample_q_product.rating
    }, format='json')
    response = view(request, pk=sample_q_product.id)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_view_set_destroy(sample_q_product):
    """Test product ViewSet destroy part, response status code 204 no content."""
    factory = APIRequestFactory()
    view = ProductsViewSet.as_view({'delete': 'destroy'})
    request = factory.delete('products/')
    response = view(request, pk=sample_q_product.id)

    assert response.status_code == 204


# Product Rating
@pytest.mark.django_db
def test_product_rating_view_set_list(sample_q_product_rating, sample_q_user):
    """Test product rating ViewSet list part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductRatingViewSet.as_view({'get': 'list'})
    request = factory.get('product-rating/')
    request.user = sample_q_user
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_rating_view_set_retrieve(sample_q_product_rating, sample_q_user):
    """Test product rating ViewSet retrieve part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductRatingViewSet.as_view({'get': 'retrieve'})
    request = factory.get('product-rating/')
    request.user = sample_q_user
    response = view(request, pk=sample_q_product_rating.id)

    assert response.status_code == 200



@pytest.mark.django_db
def test_product_rating_view_set_create(sample_q_user, sample_q_product):
    """Test product rating ViewSet create part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductRatingViewSet.as_view({'post': 'create'})
    request = factory.post('product-rating/', {
        'id': '',
        'user': sample_q_user.id,
        'product': sample_q_product.id,
        'product_rating': 1.0
    }, format='json')
    request.user = sample_q_user
    response = view(request)

    assert response.status_code == 201


@pytest.mark.django_db
def test_product_rating_view_set_update(sample_q_product_rating, sample_q_user):
    """Test product rating ViewSet update part, response status code 200 ok."""
    factory = APIRequestFactory()
    view = ProductRatingViewSet.as_view({'put': 'update'})
    request = factory.put('product-rating/', {
        'id': '',
        'user': sample_q_product_rating.user.id,
        'product': sample_q_product_rating.product.id,
        'product_rating': sample_q_product_rating.product_rating
    }, format='json')
    request.user = sample_q_user
    response = view(request, pk=sample_q_product_rating.id)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_rating_view_set_destroy(sample_q_product_rating, sample_q_user):
    """Test product rating ViewSet destroy part, response status code 204 no content."""
    factory = APIRequestFactory()
    view = ProductRatingViewSet.as_view({'delete': 'destroy'})
    request = factory.delete('product-rating/')
    request.user = sample_q_user
    response = view(request, pk=sample_q_product_rating.id)

    assert response.status_code == 204