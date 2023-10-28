from django.shortcuts import render
from order.models import Order

# Create your views here.
def member_orderlist_view(request):
    return render(request, 'member_orderlist.html')
