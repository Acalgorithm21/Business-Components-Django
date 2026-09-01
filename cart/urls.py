from cart.views import ReturnCartView
from django.urls import path


urlpatterns = [
    path('cart/addProduct/', ReturnCartView.as_view(), name='add_product'),
    path('cart/list/', ReturnCartView.as_view(), name='cart_list')

]