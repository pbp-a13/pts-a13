from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('member_orderlist/', member_orderlist_view, name='member_orderlist'),
    path('apply_sort/', apply_sort, name='apply_sort'),
    path('all_books/', all_books, name='all_books'),
    path('get_book/', get_book, name='get_book'),
    path('show_all_orders/', show_all_orders, name='show_all_orders'),
    path('show_user_orders/', show_user_orders, name='show_user_orders'),
    path('make_order/', make_order, name='make_order'),
    path('add_order/', add_order, name='add_order'),
    path('minus_order/', minus_order, name='minus_order'),
    path('complete_order/', complete_order, name='complete_order'),
]