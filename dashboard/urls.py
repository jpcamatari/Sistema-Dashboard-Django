from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lancar', views.lancar, name="lancar"),
    path('total_gasto', views.total_gasto, name="total_gasto"),
    path('relatorio_gasto', views.relatorio_gasto, name='relatorio_gasto'),
    path('relatorio_categoria',views.relatorio_categoria, name="relatorio_categoria"),
    ]