from django.db.models import Avg
from products.models import (
    Product,
    ProductRating
)


def calculate_product_rating(product: Product):
    """Calculate product rating and save it's instance.
    """
    _rating = ProductRating.objects.filter(product=product).aggregate(Avg('product_rating'))
    if _rating['product_rating__avg']:
        product.rating = _rating['product_rating__avg']
    else:
        product.rating = 0
    product.save()