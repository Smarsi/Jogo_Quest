from django.db import models
from .base import Base

class CategoriaPerguntas(Base):
    nome_categoria = models.CharField('Categoria', max_length=50)

    class Meta:
        verbose_name = 'Categoria de Perguntas'
        verbose_name_plural = 'Categorias de Perguntas'

    def __str__(self):
        return self.nome_categoria