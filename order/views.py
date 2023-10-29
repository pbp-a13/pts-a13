from django.shortcuts import render
from order.models import Order
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
@login_required
def member_orderlist_view(request):
    return render(request, 'member_orderlist.html')

def order_details(request, id):
    data = Order.objects.filter(pk=id)
    return JsonResponse(serializers.serialize("json", data), safe=False)
