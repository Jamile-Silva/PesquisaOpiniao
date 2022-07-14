# Generated by Django 4.0.3 on 2022-07-12 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePermissao', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTipoPergunta', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=50)),
                ('senhaUsuario', models.CharField(max_length=20)),
                ('edvUsuario', models.CharField(max_length=15)),
                ('admUsuario', models.BooleanField()),
                ('fkPermissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomePesquisa+', to='pesquisa.permissao')),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePesquisa', models.CharField(max_length=50)),
                ('criador', models.CharField(max_length=50)),
                ('anonimo', models.BooleanField()),
                ('fkPermissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomePermissao+', to='pesquisa.permissao')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=150)),
                ('fkPesquisa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomePesquisa+', to='pesquisa.pesquisa')),
                ('fkResposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resposta+', to='pesquisa.resposta')),
                ('fkTipoPergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomeTipoPergunta+', to='pesquisa.tipopergunta')),
            ],
        ),
    ]
