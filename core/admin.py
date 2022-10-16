from django.contrib import admin
from .models import *

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['categoria_perguntas', 'pontuacao']
