from django.shortcuts import render
from order.models import Order

def cart(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    
    book_quantities = {}

    for order in orders:
        book = order.book
        quantity = order.quantity

        if book not in book_quantities:
            book_quantities[book] = quantity
        else:
            book_quantities[book] += quantity
            
    total_price = sum(order.subtotal() for order in orders)

    return render(request, 'cart.html', {'book_quantities': book_quantities, 'total_price': total_price})
