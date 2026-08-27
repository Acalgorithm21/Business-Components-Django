from django.db import models

from products.models import Product
from config import settings

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(default=0)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)