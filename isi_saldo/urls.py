from django.urls import path
from . import views

urlpatterns = [
    path('top-up-balance/', views.top_up_balance, name='top_up_balance'),
]
