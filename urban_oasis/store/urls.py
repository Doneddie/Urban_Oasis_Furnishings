from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('cart/', views.cart_view, name='cart'),
     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
