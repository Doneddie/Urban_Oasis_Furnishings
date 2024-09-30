from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('welcome/', views.welcome, name='welcome'),
    path('about-us/', views.about_us, name='about_us'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('cart/', views.cart_view, name='cart'),
     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
