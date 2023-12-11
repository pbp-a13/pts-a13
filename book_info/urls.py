from django.urls import path
from book_info.views import show_info, edit_book, delete_book, add_to_cart, increment_amount, decrement_amount, get_cart_json, get_review_json, search_review_json

app_name = 'book_info'

urlpatterns = [
    path('<int:id>/', show_info, name='show_info'),
    path('edit-book/<int:id>/', edit_book, name='edit_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
    path('add-to-cart/<int:id>/<int:amount>/', add_to_cart, name='add_to_cart'),
    path('increment-amount/<int:id>/', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:id>/', decrement_amount, name='decrement_amount'),
    path('get-cart/', get_cart_json, name='get_cart_json'),
    path('get-review/<int:id>/', get_review_json, name='get_review_json'),
    path('search-review/<rating>/', search_review_json, name ='search_review_json'),
]