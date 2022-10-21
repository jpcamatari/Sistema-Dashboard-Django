from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('total_gasto', views.total_gasto, name="total_gasto"),
    ]