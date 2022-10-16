from django.db import models

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add = True)
    modificado = models.DateField('Modificado', auto_now = True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True