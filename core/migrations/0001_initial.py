# Generated by Django 4.1.2 on 2022-10-12 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]
