from django.shortcuts import render
from order.models import Order
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def member_orderlist_view(request):
    return render(request, 'member_orderlist.html')

def order_id(request, id):
    data = Order.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")