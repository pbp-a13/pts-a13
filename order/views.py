from django.shortcuts import render
from .models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def member_orderlist_view(request):
    return render(request, 'member_orderlist.html')

@csrf_exempt
def update_order(request):
    if request.is_ajax() and request.method == "POST":
        order_id = request.POST.get('order_id', None)
        if order_id:
            try:
                order = Order.objects.get(pk=order_id)
                order.is_completed = True
                order.save()
                data = {'is_completed': True}
                return JsonResponse(data)
            except Order.DoesNotExist:
                return JsonResponse({"error": "Order not found"}, status=404)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


