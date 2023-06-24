from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('tasks/', views.tasks, name='tasks'),
    path('plan/', views.plan, name='plan'),
]
