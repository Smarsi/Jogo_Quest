from django.db import models
from .base import Base

class Alternativas(Base):
    pergunta = models.ForeignKey('core.Perguntas', verbose_name='PerguntaRelacionada', on_delete=models.CASCADE)
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
    resposta = models.CharField('Resposta', max_length=150)
    #alternativas = models.CharField(max_length=150, choices=CHOICE_LIST, null=True)

    #Relacionamentos
    categoria_pergunta = models.ForeignKey('core.CategoriaPerguntas', verbose_name='Categoria', on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'Pergunta'
        verbose_name_plural = 'Perguntas'
    
    def __str__(self):
        return str(self.pk)
