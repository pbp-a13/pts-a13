from django.forms import ModelForm
from order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["title", "quantity", "order_date", "price", "estimated_delivery_date"]