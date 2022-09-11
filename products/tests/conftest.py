import pytest
from django.contrib.auth.models import User
from products.models import (
    Product,
    ProductRating
)


@pytest.fixture
def sample_q_user(db):
    return User.objects.create_user(
        username='SampleUser',
        email='sample@email.com',
        password='password',
        first_name='FirstName',
        last_name='LastName'
    )

@pytest.fixture
def sample_q_product(db):
    return Product.objects.create(
        name='SampleProduct',
        price='1.00',
        rating=0.0
    )

@pytest.fixture
def sample_q_product_rating(db, sample_q_user, sample_q_product):
    return ProductRating.objects.create(
        product=sample_q_product,
        user=sample_q_user,
        rating=3.0
    )