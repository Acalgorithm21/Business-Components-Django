from rest_framework import serializers

from cart.models import Cart
from .models import User
from django.contrib.auth import authenticate

#Serialzier determines what data the API is allowed to receive
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        cart = Cart.objects.create(
            user=user
        )


        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['email'],
            password=data['password']
        )
        if user is None:
            raise serializers.ValidationError({'password': ''})

        data['user'] = user
        return data



class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def update(self, instance,validated_data):

        if 'first_name' in validated_data:
            instance.first_name = validated_data['first_name']

        if 'last_name' in validated_data:
            instance.last_name = validated_data['last_name']

        if 'email' in validated_data:
            instance.email = validated_data['email']

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()

        return instance