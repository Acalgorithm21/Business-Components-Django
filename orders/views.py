from django.shortcuts import render
from django.views import generic
from rest_framework import permissions

from orders.models import Order
from serializers import CreateOrderSerializer

# Create your views here.

##OrderViews
class CCreateOrder(generic.CreateView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]




##OrderItemViews