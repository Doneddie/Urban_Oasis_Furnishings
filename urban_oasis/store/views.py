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
    # Cart handling logic here
    pass

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

     # Check if there is an active order in the session or create a new one
    order_id = request.session.get('order_id')
    
    if order_id:
        # Try to retrieve the existing order
        order = Order.objects.get(id=order_id)
    else:
        # No order exists, create a new one
        order = Order.objects.create(
            customer_name="Guest", 
            customer_email="guest@example.com",  # Example, update for real users
            address="Guest Address", 
            total_amount=0  # I'll need to update this later
        )
        # Save the new order ID in the session
        request.session['order_id'] = order.id

    # Now that you have an order, create the order item
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1
        
        # Create the OrderItem and associate it with the order
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

        # Update the order total amount based on the product price
        order.total_amount += product.price * quantity
        order.save()

        return redirect('cart')  # Redirect to the cart page or wherever
    else:
        return HttpResponse("Invalid request method")

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
