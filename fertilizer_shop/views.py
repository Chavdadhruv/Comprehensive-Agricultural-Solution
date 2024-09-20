# fertilizer_shop/views.py

from django.shortcuts import render, get_object_or_404
from .models import Fertilizer

def fertilizer_shop(request):
    fertilizers = Fertilizer.objects.all()
    return render(request, 'shop.html', {'fertilizers': fertilizers})

def add_to_cart(request, fertilizer_id):
    fertilizer = get_object_or_404(Fertilizer, id=fertilizer_id)
    # Implement cart logic here
    # For simplicity, this is just a placeholder
    return render(request, 'cart.html', {'fertilizer': fertilizer})

def buy_now(request, fertilizer_id):
    fertilizer = get_object_or_404(Fertilizer, id=fertilizer_id)
    # Implement buy logic here
    # For simplicity, this is just a placeholder
    return render(request, 'buy_confirmation.html', {'fertilizer': fertilizer})
