from django.db import models

from orders.models import Order


# Create your models here.
class Shipping(models.Model):
    order = models.OneToOneField(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='shipping',
    )

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=200)

