
from django.shortcuts import render, get_object_or_404
from .models import Products, Order, Items
from django.contrib.auth.decorators import login_required

def home(request):
    
    return render(request, 'index.html')
