from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UsuariosPartidaInline(admin.TabularInline):
    model = UsuarioPartida
    max_num = 2

class UsuariosPerguntasInline(admin.TabularInline):
    model = PerguntasUsuarioPartida

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'vencedor']
    inlines = [UsuariosPartidaInline,]

@admin.register(UsuarioPartida)
class UsuarioPartidaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'partida', 'pontuacao', ]
    inlines = [UsuariosPerguntasInline,]
    list_filter = ('partida',)

'''
@admin.register(PerguntasUsuarioPartida)
class PerguntasUsuarioPartidaAdmin(admin.ModelAdmin):
    list_display = ['status', 'pergunta', 'usuarioPartida']
'''


@admin.register(CategoriaPerguntas)
class CategoriaPerguntas(admin.ModelAdmin):
    list_display = ['nome_categoria']

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'tema_pergunta']
    list_filter = ('tema_pergunta',)

@admin.register(Pontuacao)
class RankingAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pontos']
    list_filter = ('usuario', 'pontos')

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'imagem']

@admin.register(Peao)
class PeaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'imagem']