from django.urls import path
from .views import CreateProduct


urlpatterns = [

    path('product/', CreateProduct.as_view(), name='product'),

]
