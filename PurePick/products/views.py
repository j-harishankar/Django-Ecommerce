
from django.shortcuts import render, get_object_or_404
from .models import Products, Order, Items
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def product_list(request):
    products = Products.objects.filter(delete_status=1).order_by('priority')
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id, delete_status=1)
    return render(request, 'product_details.html', {'product': product})

@login_required
def cart(request):
    customer = request.user.customer_profile
    cart = Order.objects.filter(owner=customer, order_status=0).first()
    items = cart.added_carts.all() if cart else []
    return render(request, 'cart.html', {'items': items})

@login_required
def checkout(request):
    return render(request, 'checkout.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def account_view(request):
    return render(request, 'account.html')
