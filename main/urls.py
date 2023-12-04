from django.urls import path
from main.views import show_main
from main.views import get_book_json
from main.views import search_book_json
from account.views import login_user
from main.views import switch_mode
from main.views import show_json
from main.views import search_book_flutter



app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-book/<sort_mode>', get_book_json, name='get_book_json'),
    path('search-book/<search_mode>/<sort_mode>', search_book_json, name ='search_book_json'),
    path('switch-mode', switch_mode, name="switch_mode"),
    path('json/', show_json, name='show_json'), 
    path('json-flutter/<value>/<search_mode>/<sort_mode>', search_book_flutter, name = 'search_book_flutter'),
]