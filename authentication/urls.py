from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('get_account', get_account, name='get_account'),
    path('update_account', update_account, name='update_account'),
    path('get_all_members/', get_all_members, name='get_all_members'),
]