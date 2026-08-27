from django.db import models


# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='payments',
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

