from django.db import models
from .base import Base

#Import Relacionamentos
from .tema import Tema


class Perguntas(Base):
    CHOICE_LIST = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    
    pergunta = models.CharField('Pergunta', max_length=50)
    alternativa1 = models.CharField('1_alternativa', max_length=750, null=False, blank=False)
    alternativa2 = models.CharField('2_alternativa', max_length=750, null=False, blank=False)
    alternativa3 = models.CharField('3_alternativa', max_length=750, null=False, blank=False)
    alternativa4 = models.CharField('4_alternativa', max_length=750, null=False, blank=False)
    alternativa5 = models.CharField('5_alternativa', max_length=750, null=False, blank=False)
    resposta = models.IntegerField('Alternativa Correta', choices=CHOICE_LIST)

    #Relacionamentos
    tema_pergunta = models.ForeignKey('core.Tema', verbose_name='Tema', on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'Pergunta'
        verbose_name_plural = 'Perguntas'
    
    def __str__(self):
        return str(self.pk)
