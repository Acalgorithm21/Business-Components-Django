from django.shortcuts import render
from rest_framework import generics, permissions

from cart.models import Cart, CartItem
from cart.serializers import CartITEMSerializer
from rest_framework import permissions


# Create your views here.

##Add an item to the cart API
##TEST FIELDS ['product'(INT), 'quantity' (INT)]
class AddProductView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny] ## Temporary for testing purposes
    queryset = CartItem.objects.all()
    serializer_class = CartITEMSerializer

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)

##Return list of items
class ReturnCartView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartITEMSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=cart)


