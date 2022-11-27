from django.db import models
from .base import Base  

# Import de Relacionamentos
from django.contrib.auth.models import User
from .perguntas import Perguntas


class Partida(Base):
    STATUS_CHOICES = (
        ('0', 'Aguardando Inicio'),
        ('1', 'Iniciada'),
        ('2', 'Finalizada')
    )

    usuarioPartida = models.ManyToManyField(User, related_name='UsuarioPartida', through='UsuarioPartida')
    status = models.CharField('Status', max_length=5, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])

    #Relationships
    vencedor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return str(self.pk)



# --------------- Relacionamentos ManyToMany -----------------

class UsuarioPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT, related_name='usuario_partida')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_partida')
    pontuacao = models.IntegerField('Pontuação', null=True, blank=True)
    
    perguntas = models.ManyToManyField(Perguntas, related_name='PerguntasUsuarioPartida', through="PerguntasUsuarioPartida")

    def __str__(self):
        return str(self.usuario)

class PerguntasUsuarioPartida(models.Model):
    STATUS_CHOICES = (
        ('0', 'Não Respondida'),
        ('1', 'Respondida Errado'),
        ('2', 'Respondida Corretamente')
    )

    usuarioPartida = models.ForeignKey(UsuarioPartida, on_delete=models.PROTECT, related_name='perguntas_usuario_partida')
    pergunta = models.ForeignKey(Perguntas, on_delete=models.PROTECT, related_name='perguntas_usuario_partida')
    status = models.CharField('Status', max_length=25, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])

    def __str__(self):
        return str(self.usuarioPartida)


