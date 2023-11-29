from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from book.views import *


app_name = 'book'

urlpatterns = [
    path('add-book', add_book, name='add_book'),
    path("", get_books, name="get_books")
]



# image settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

