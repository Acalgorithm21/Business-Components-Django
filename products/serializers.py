from rest_framework import serializers
from .models import Product



###Serializer for creating products
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

###Serializer for list returning a list of products
class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']


###Serializer for getting product by ID
class ProductByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']


###Serializer for updating products
class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)


        instance.save()

        return instance

