from django.contrib import admin
from .models import *

class UsuariosPartidaInline(admin.TabularInline):
    model = UsuarioPartida

class UsuariosPerguntasInline(admin.TabularInline):
    model = PerguntasUsuarioPartida

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pontuacao', 'status']
    inlines = [UsuariosPartidaInline,]

@admin.register(UsuarioPartida)
class UsuarioPartidaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'partida', 'resultado', ]
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

class AlternativasInLine(admin.TabularInline):
    model = Alternativas

@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'resposta']
    inlines = [AlternativasInLine,]

@admin.register(Alternativas)
class AlternativasAdmin(admin.ModelAdmin):
    list_display = ['resposta', 'pergunta', 'correta']
    list_filter = ('pergunta', 'correta')