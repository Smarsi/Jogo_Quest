from django.db import models
from .base import Base

# Import de Relacionamentos
from django.contrib.auth.models import User

class Pontuacao(Base):
    pontos = models.IntegerField('Pontuação')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Ranking'

    def __str__(self):
        return str(self.usuario)