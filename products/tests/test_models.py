import pytest
from products.models import (
    Product,
    ProductRating
)


@pytest.mark.django_db
def test_product_model():
    product = Product.objects.create(
        name='SampleProduct',
        price='1.00',
        rating=0.0
    )

    assert isinstance(product, Product)
    assert product.name == 'SampleProduct'
    assert product.price == '1.00'
    assert product.rating == 0.0


@pytest.mark.django_db
def test_product_rating_model(sample_q_product, sample_q_user):
    pr_rating = ProductRating.objects.create(
        product=sample_q_product,
        user=sample_q_user,
        product_rating=3.0
    )

    assert isinstance(pr_rating, ProductRating)
    assert pr_rating.product == sample_q_product
    assert pr_rating.user == sample_q_user
    assert pr_rating.product_rating == 3.0
