from django.urls import path
from book_info.views import add_to_cart_flutter, book_review_json, delete_book_flutter, edit_book_flutter, filter_review_flutter, get_cart_json_flutter, show_info, edit_book, delete_book, add_to_cart, increment_amount, decrement_amount, get_cart_json, get_review_json, sort_review_json, show_json_by_id, sort_review_flutter

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
    path('sort-review/<sort_mode>/', sort_review_json, name ='sort_review_json'),
    path('edit-flutter/<int:id>/', edit_book_flutter, name='edit_book_flutter'),
    path('add-to-cart-flutter/<int:id>/<int:amount>/', add_to_cart_flutter, name='add_to_cart_flutter'),
    path('filter-review-flutter/', filter_review_flutter, name='filter_review_flutter'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-book-review/<int:id>/', book_review_json, name='book_review_json'),
    path('delete-flutter/<int:id>/', delete_book_flutter, name='delete_book_flutter'),
    path('sort-review-flutter/<sort_mode>', sort_review_flutter, name ='sort_review_flutter'),
    path('get-cart-flutter/', get_cart_json_flutter, name='get_cart_json_flutter'),
]