from django.urls import path
from book_info.views import show_info, edit_book, delete_book, increment_amount, decrement_amount

app_name = 'book_info'

urlpatterns = [
    path('<int:id>/', show_info, name='show_info'),
    path('edit-book/<int:id>', edit_book, name='edit_book'),
    path('delete/<int:id>', delete_book, name='delete_book'),
    path('increment-amount/<int:book_id>/', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:book_id>/', decrement_amount, name='decrement_amount'),
]