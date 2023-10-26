from django.urls import path
from book_info.views import show_info

app_name = 'book_info'

urlpatterns = [
    path('', show_info, name='show_info'),
]