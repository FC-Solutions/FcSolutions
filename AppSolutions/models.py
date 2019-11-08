from django.db import models
from django.contrib.auth.models import User

#USER: admin SENHA: admin


class Colaborador(models.Model):
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
    nome = models.CharField(max_length=128, default='')
    usuario = models.ForeignKey(User, verbose_name='Autor', on_delete=models.DO_NOTHING)
    seguidores = models.ManyToManyField("Colaborador", verbose_name='Seguidores', blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Publicacao(models.Model):
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Colaborador, verbose_name='Autor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto

class Comentario(models.Model):
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Colaborador, related_name='autor', on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(Publicacao, related_name='publicacao', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto