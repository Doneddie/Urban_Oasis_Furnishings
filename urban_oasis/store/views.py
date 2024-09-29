from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    # Cart handling logic here
    pass

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Logic to add the product to the cart
    # Example:
    cart = Cart.objects.get(user=request.user)
    cart.add(product)

    return redirect('cart')  # Redirect to the cart page after adding the item

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
