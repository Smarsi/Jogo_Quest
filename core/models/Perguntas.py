from django.db import models
from .Base import Base

class Perguntas(Base):
    ALTERNATIVAS_CHOICES = (
        ('alternativa1', 'resposta1'),
        ('alternativa2', 'resposta2'),
    )


    pergunta = models.CharField(max_length=50)
    resposta = models.CharField(max_length=50)
    alternativas = models.CharField(max_length=50, choices = ALTERNATIVAS_CHOICES)

    #Relacionamentos
    categoria_pergunta = models.ForeignKey('core.CategoriaPerguntas', verbose_name='Categoria', on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'Pergunta'
        verbose_name_plural = 'Perguntas'
    
    def __str__(self):
        return self.id