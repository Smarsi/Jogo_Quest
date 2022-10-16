# Generated by Django 4.1.2 on 2022-10-16 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPerguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome_categoria', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria de Perguntas',
                'verbose_name_plural': 'Categorias de Perguntas',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Pontuação')),
                ('categoria_perguntas', models.CharField(max_length=50, verbose_name='Categoria')),
                ('jogador1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jogador1', to=settings.AUTH_USER_MODEL)),
                ('jogador2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jogador2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pergunta', models.CharField(max_length=50)),
                ('resposta', models.CharField(max_length=50)),
                ('alternativas', models.CharField(choices=[('alternativa1', 'resposta1'), ('alternativa2', 'resposta2')], max_length=50)),
                ('categoria_pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriaperguntas', verbose_name='Categoria')),
            ],
            options={
                'verbose_name_plural': 'Perguntas',
            },
        ),
        migrations.CreateModel(
            name='PerguntasPartida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='perguntas_partida', to='core.partida')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='perguntas_partida', to='core.perguntas')),
            ],
        ),
        migrations.AddField(
            model_name='partida',
            name='perguntas',
            field=models.ManyToManyField(related_name='PerguntasPartida', through='core.PerguntasPartida', to='core.perguntas'),
        ),
    ]
