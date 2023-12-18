from django.urls import path
from main.views import delete_book_flutter, get_review_json, show_json_by_id, show_main
from main.views import get_book_json
from main.views import search_book_json
from account.views import login_user
from main.views import switch_mode
from main.views import show_json
from main.views import search_book_flutter
from main.views import show_admin_json
from main.views import switch_mode_flutter


app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-book/<sort_mode>', get_book_json, name='get_book_json'),
    path('search-book/<search_mode>/<sort_mode>', search_book_json, name ='search_book_json'),
    path('switch-mode', switch_mode, name="switch_mode"),
    path('json/', show_json, name='show_json'), 
    path('json-flutter/<value>/<search_mode>/<sort_mode>', search_book_flutter, name = 'search_book_flutter'),
    path('show_admin_json/', show_admin_json, name='show_admin_json'),
    path('switch_mode_flutter', switch_mode_flutter, name = 'switch_mode_flutter'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-review/<int:id>/', get_review_json, name='get_review_json'),
    path('delete-flutter/<int:id>/', delete_book_flutter, name='delete_book_flutter'),
]