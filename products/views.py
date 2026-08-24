from rest_framework import generics, permissions

from .models import Product
from .serializers import CreateProductSerializer


# Create your views here.

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.IsAuthenticated]


    