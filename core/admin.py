from django.contrib import admin
from .models import *

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria_perguntas', 'pontuacao']

@admin.register(CategoriaPerguntas)
class CategoriaPerguntas(admin.ModelAdmin):
    list_display = ['nome_categoria']

@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'resposta']