from django.db import models
from .Base import Base  

# Import de Relacionamentos
from django.contrib.auth.models import User
from .perguntas import Perguntas


class Partida(Base):
    pontuacao = models.DecimalField('Pontuação', max_digits=8, decimal_places=2, blank=False, null=False)
    jogador1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='jogador1')
    jogador2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='jogador2')

    Perguntas = models.ManyToManyField(Perguntas, related_name='PerguntasPartida', through="PerguntasPartida")



# --------------- Relacionamentos ManyToMany -----------------

class PerguntasPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT, related_name='PerguntasPartida)
    pergunta = models.ForeignKey(Partida, on_delete=models.PROTECT, related_name='PerguntasPartida)