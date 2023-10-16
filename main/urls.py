from django.urls import path
from main.views import show_main
from main.views import get_book_json


app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-book/', get_book_json, name='get_book_json'),
]