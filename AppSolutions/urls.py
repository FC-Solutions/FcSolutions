from django.urls import path

from AppSolutions import views
from .views import HomePageView, inicio, PublicacaoView, Perfil, Seguir, ComentarioView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', PublicacaoView.as_view(), name='publicar'),
    path('perfil/<str:nome>/', Perfil, name='perfil'),
    path('seguir/<int:id_colaborador>', Seguir, name='seguir'),
    path('<int:publica_id>', views.Detalhe, name='detalhe'),
    path('comentar/<int:id_publicacao>', ComentarioView.as_view(), name='comentar'),
] 