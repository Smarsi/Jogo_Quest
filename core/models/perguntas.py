from django.db import models
from .base import Base

#Import Relacionamentos
from .tema import Tema

class Alternativas(Base):
    pergunta = models.ForeignKey('core.Perguntas', verbose_name='Pergunta Relacionada', on_delete=models.CASCADE)
    resposta = models.CharField('Resposta', max_length=150)
    correta = models.BooleanField('Correta?', default=False)

    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

    def __str__(self):
        return self.resposta

class Perguntas(Base):
    CHOICE_LIST = Alternativas.objects.all()
    
    pergunta = models.CharField('Pergunta', max_length=50)

    #Relacionamentos
    tema_pergunta = models.ForeignKey('core.Tema', verbose_name='Tema', on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name: 'Pergunta'
        verbose_name_plural = 'Perguntas'
    
    def __str__(self):
        return str(self.pk)
