from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('member_orderlist/', member_orderlist_view, name='member_orderlist'),
    path('details', order_details, name='details')

]