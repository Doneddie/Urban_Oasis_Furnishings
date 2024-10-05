from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from .forms import OrderForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def welcome(request):
    return render(request, 'store/welcome.html')

def about_us(request):
    return render(request, 'store/about_us.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'store/register.html', {'form': form})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    # Get the product object from the database
    product = get_object_or_404(Product, id=product_id)

    # Get the current cart from the session or initialize an empty one
    cart = request.session.get('cart', {})

    # Store product details in the cart (product ID as the key)
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1  # Increase quantity if already in the cart
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image': product.image.url if product.image else ''
        }

    # Save the cart back into the session
    request.session['cart'] = cart
    request.session.modified = True  # Ensure the session is marked as modified
    
    return redirect('cart')  # Redirect to the cart page or wherever

def cart(request):
    # Get the cart from session (initialize as empty if it doesn't exist)
    cart = request.session.get('cart', {})

    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    
    return render(request, 'store/cart.html', {'cart_items': cart, 'total': total})


def cart_view(request):
    # Logic for the cart page
    return render(request, 'store/cart.html')

def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Process cart items and save order items
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'store/checkout.html', {'form': form})

def order_success(request):
    return render(request, 'store/order_success.html')
