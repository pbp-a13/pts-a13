from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('account_info/', account_info, name='account_info'),
    path('all_member_page/', all_member_page, name='all_member_page'),
    path('member_details/<int:member_id>/', member_details, name='member_details'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user')
]