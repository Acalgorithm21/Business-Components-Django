from rest_framework import serializers
from .models import Order
from .models import OrderItem

##Order Serializers
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer']

    def create(self, validated_data):
        order_number = validated_data['order_number']
        customer = validated_data['customer']

        order = Order.objects.create(
            order_number=order_number,
            customer=customer
        )

        return order

##orderItem Serializers
class AddOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']
