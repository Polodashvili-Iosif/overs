from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('plan/', views.plan, name='plan'),
    path('my_plan/', views.my_plan, name='my_plan'),
    path('map/', views.map, name='map'),
]
