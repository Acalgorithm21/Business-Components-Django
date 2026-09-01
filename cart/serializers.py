from rest_framework import serializers

from cart.models import Cart, CartItem
from users.models import User



##Cart-Item serializers
class CartITEMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

