from django.db import models
from .base import Base  

# Import de Relacionamentos
from django.contrib.auth.models import User
from .perguntas import Perguntas


class Partida(Base):
    pontuacao = models.DecimalField('Pontuação', max_digits=8, decimal_places=2, blank=False, null=False)
    jogador1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='jogador1')
    jogador2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='jogador2')
    categoria_perguntas = models.CharField('Categoria', max_length=50)

    perguntas = models.ManyToManyField(Perguntas, related_name='PerguntasPartida', through="PerguntasPartida")



# --------------- Relacionamentos ManyToMany -----------------

class PerguntasPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT, related_name='perguntas_partida')
    pergunta = models.ForeignKey(Perguntas, on_delete=models.PROTECT, related_name='perguntas_partida')