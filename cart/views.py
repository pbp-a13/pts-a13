from django.shortcuts import render, redirect
from .models import CartItem # order belom

def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
