from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import PublicacaoForm, ComentarioForm
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = 'AppSolutions/home.html'

def inicio(request):
    colaborador = Colaborador.objects.get(usuario=request.user)
    seguidores = colaborador.seguidores.all()
    publicacoes = Publicacao.objects.filter(autor__in=seguidores)
    
    return render(request, 'AppSolutions/inicio.html',{'publicacoes': publicacoes})

class PublicacaoView(FormView):
    template_name = 'AppSolutions/publicar.html'
    form_class = PublicacaoForm

    def form_valid(self, form):
        dados = form.clean()
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        publicacao = Publicacao(texto=dados['texto'], autor=colaborador)
        publicacao.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')

class ComentarioView(FormView):
    template_name = 'AppSolutions/comentar.html'
    form_class = ComentarioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub = Publicacao.objects.get(pk=self.kwargs['id_publicacao'])        
        context['publicacao'] = pub        
        return context
    
    def form_valid(self, form):
        id_publicacao = self.kwargs['id_publicacao']
        dados = form.clean()
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        publicacao1 = Publicacao.objects.get(id=id_publicacao)
        comentario = Comentario(texto=dados['texto'], autor=colaborador, publicacao=publicacao1)
        comentario.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')


def Perfil(request, nome):
    try:
        colaborador_log = Colaborador.objects.get(usuario=request.user)
        colaborador = Colaborador.objects.get(usuario__username=nome)
        publicacoes = Publicacao.objects.filter(autor=colaborador).order_by('-data')
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'AppSolutions/perfil.html', {'publicacoes': publicacoes, 'colaborador': colaborador, 'colaborador_log':colaborador_log, 'nome':nome})

def Seguir(request, id_colaborador):
    try:
        colaborador = Colaborador.objects.get(usuario=request.user)
        cara_quero_seguir = Colaborador.objects.get(pk=id_colaborador)
        colaborador.seguidores.add(cara_quero_seguir)

    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')
    
    return render(request, 'AppSolutions/sucesso_seguir.html', {'cara_quero_seguir': cara_quero_seguir})

def Detalhe(request, public_id):
    try:
        publicacao = Publicacao.objects.get(pk=public_id)
        comentari = Comentario.objects.get(publicacao=public_id)
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')
    return render(request, 'AppSolutions/detalhe.html', {'publicacao':publicacao, 'comentari':comentari})