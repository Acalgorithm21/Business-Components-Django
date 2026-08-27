from django.urls import path
from .views import CreateProduct, ProductList, ProductByID, UpdateProduct, DeleteProduct, SearchProducts

urlpatterns = [

    path('product/', CreateProduct.as_view(), name='product'),
    path('product/productList/', ProductList.as_view(), name='product-list'),
    path('product/productByID/<int:pk>/', ProductByID.as_view(), name='product-create'),
    path('product/update/<int:pk>/', UpdateProduct.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', DeleteProduct.as_view(), name='product-delete'),
    path('product/search/', SearchProducts.as_view(), name='product-search'),

]

