from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .contrib.calculate_rating import calculate_product_rating


class Product(models.Model):
    name = models.CharField(max_length=150, help_text='Name of the product', unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, help_text='Product price.')
    rating = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    updated_at = models.DateTimeField(auto_now=True)


class ProductRating(models.Model):
    class Meta:
        unique_together = ('product', 'user')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_rating = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])


@receiver(post_save, sender=ProductRating)
def product_rating_post_save(sender, instance, created, **kwargs):
    """Calculate product rating after save.
    """
    calculate_product_rating(instance.product)


@receiver(post_delete, sender=ProductRating)
def product_rating_post_delete(sender, instance, **kwargs):
    """Calculate product rating after delete.
    """
    calculate_product_rating(instance.product)