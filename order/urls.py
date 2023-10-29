from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('member_orderlist/', member_orderlist_view, name='member_orderlist'),
    path('update_order/', update_order, name='update_order'),

]