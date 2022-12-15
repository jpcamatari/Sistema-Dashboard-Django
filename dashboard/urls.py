from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lancar', views.lancar, name="lancar"),
    path('total_gasto', views.total_gasto, name="total_gasto"),
    path('relatorio_gasto', views.relatorio_gasto, name='relatorio_gasto'),
    ]

#URL 'lancar' - Pagina html do formulario resposavel por enviar informações para o banco de dados;
#URL '' - Pagina html da home, onde é gerada os graficos e tabelas;
#URL 'total_gasto' - Retorna a somatoria do valor total gasto em JSON;
#URL 'relatorio_gasto' - Retorna a somatoria dos gastos mes a mes em JSON;