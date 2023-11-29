from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('account_info/', account_info, name='account_info'),
    path('all_member_page/', all_member_page, name='all_member_page'),
    path('member_details/<int:member_id>/', member_details, name='member_details'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('get_account_info/', get_account_info, name='get_account_info'),
    path('update_account_info/', update_account_info, name='update_account_info'),
    path('search-members/', search_members, name='search_members'),
    path('get_all_member_info/', get_all_members, name='get_all_member_info'),
    path('register_flutter/', register_flutter, name='register_flutter'),
]