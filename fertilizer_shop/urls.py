# fertilizer_shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('fertilizer_shop/', views.fertilizer_shop, name='fertilizer_shop'),
    path('add_to_cart/<int:fertilizer_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy_now/<int:fertilizer_id>/', views.buy_now, name='buy_now'),
]
