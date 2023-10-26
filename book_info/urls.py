from django.urls import path
from book_info.views import show_info, increment_amount, decrement_amount

app_name = 'book_info'

urlpatterns = [
    path('', show_info, name='show_info'),
    path('increment-amount/<int:book_id>/', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:book_id>/', decrement_amount, name='decrement_amount'),
]