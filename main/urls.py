from django.urls import path
from main.views import show_main
from main.views import get_book_json
from main.views import search_book_json


app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-book/<sort_mode>', get_book_json, name='get_book_json'),
    path('search-book/<search_mode>/<sort_mode>', search_book_json, name ='search_book_json')
]