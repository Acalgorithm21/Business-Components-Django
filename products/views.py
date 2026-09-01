from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Product
from .serializers import CreateProductSerializer, UpdateProductSerializer, ListProductSerializer, ProductByIdSerializer


# Create your views here.

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [permissions.AllowAny] ##Temporary for testing purposes only

##Returns a List of products in database
##TESTING [0 FIELDS to be sent to the database, only data to be returned]
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

class ProductByID(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductByIdSerializer
    permission_classes = [permissions.AllowAny] ## Temporary for testing purposes only

class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    permission_classes = [permissions.AllowAny] ##Temporary for testing purposes only

class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny] ##Temporary for testing purposes

class SearchProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer ##Reused

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        price = self.request.query_params.get('price')
        quantity = self.request.query_params.get('quantity')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if description:
            queryset = queryset.filter(description__icontains=description)

        if price:
            queryset = queryset.filter(price=price)

        if quantity:
            queryset = queryset.filter(quantity=quantity)

        return queryset
