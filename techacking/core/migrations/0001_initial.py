# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivoquestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo_questao', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'arquivoquestao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arquivosresposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivos_resposta', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'arquivosresposta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cursoturma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cursoturma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240, unique=True)),
                ('carga_horaria', models.SmallIntegerField()),
                ('teoria', models.DecimalField(decimal_places=0, max_digits=3)),
                ('pratica', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ementa', models.TextField()),
                ('competencias', models.TextField()),
                ('habilidades', models.TextField()),
                ('conteudo', models.TextField()),
                ('bibliografia_basica', models.TextField()),
                ('bibliografia_complemntar', models.TextField()),
            ],
            options={
                'db_table': 'disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplinaofertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=240)),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'disciplinaofertada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gradecurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'gradecurricular',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.SmallIntegerField(unique=True)),
            ],
            options={
                'db_table': 'periodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periododisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'periododisciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField()),
                ('apelido', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('data_limite_entrega', models.CharField(max_length=10)),
                ('descricao', models.TextField()),
                ('datas', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'questao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra_aluno', models.IntegerField(unique=True)),
                ('data_avaliacao', models.CharField(max_length=10)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('avaliacao', models.TextField()),
                ('descricao', models.TextField()),
                ('data_de_envio', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'resposta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'turma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=11)),
                ('tipo_usuario', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
