from django.db import models
from .base import Base  

# Import de Relacionamentos
from django.contrib.auth.models import User
from .categorias_pergunta import CategoriaPerguntas

class Tema(Base):
    nome = models.CharField('Nome Tema', max_length=100, null=False)
    categoria = models.ForeignKey('core.CategoriaPerguntas', verbose_name='Categoria do Tema', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return str(self.nome)
