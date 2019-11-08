from django.urls import path

from .views import HomePageView, inicio, PublicacaoView, Perfil, Seguir

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', PublicacaoView.as_view(), name='publicar'),
    path('perfil/<str:nome>/', Perfil, name='perfil'),
    path('seguir/<int:id_colaborador>', Seguir, name='seguir'),
] 