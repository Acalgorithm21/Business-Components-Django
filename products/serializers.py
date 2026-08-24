from rest_framework import serializers
from .models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']


    def create(self, validated_data):
        product = Product(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            quantity=validated_data['quantity']
        )

        product.save()

        return product