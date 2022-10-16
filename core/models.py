from django.db import models

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add = True)
    modificado = models.DateField('Modificado', auto_now = True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class CategoriaPerguntas(Base):
    nome_categoria = models.CharField('Categoria', max_length=50)

    class Meta:
        verbose_name = 'Categoria de Perguntas'
        verbose_name_plural = 'Categorias de Perguntas'

    def __str__(self):
        return self.nome_categoria

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


#class Partidas(Base):
