from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('member_orderlist/', member_orderlist_view, name='member_orderlist'),
    path('apply_sort/', apply_sort, name='apply_sort'),

]