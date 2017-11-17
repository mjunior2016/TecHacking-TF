# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aluno(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')
    ra = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'aluno'


class Arquivoquestao(models.Model):
    id_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_questao')
    arquivo_questao = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivoquestao'


class Arquivosresposta(models.Model):
    id_resposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='id_resposta')
    arquivos_resposta = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'arquivosresposta'
        unique_together = (('id_resposta', 'arquivos_resposta'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Curso(models.Model):
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'curso'
        unique_together = (('sigla', 'nome'),)


class Cursoturma(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'cursoturma'


class Disciplina(models.Model):
    nome = models.CharField(unique=True, max_length=240)
    carga_horaria = models.SmallIntegerField()
    teoria = models.DecimalField(max_digits=3, decimal_places=0)
    pratica = models.DecimalField(max_digits=3, decimal_places=0)
    ementa = models.TextField()  # This field type is a guess.
    competencias = models.TextField()  # This field type is a guess.
    habilidades = models.TextField()  # This field type is a guess.
    conteudo = models.TextField()  # This field type is a guess.
    bibliografia_basica = models.TextField()  # This field type is a guess.
    bibliografia_complemntar = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'disciplina'


class Disciplinaofertada(models.Model):
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'disciplinaofertada'
        unique_together = (('ano', 'semestre', 'id_disciplina'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gradecurricular(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gradecurricular'
        unique_together = (('ano', 'semestre', 'id_curso'),)


class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')

    class Meta:
        managed = False
        db_table = 'matricula'


class Periodo(models.Model):
    id_gradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='id_gradecurricular')
    numero = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'periodo'
        unique_together = (('numero', 'id_gradecurricular'),)


class Periododisciplina(models.Model):
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')

    class Meta:
        managed = False
        db_table = 'periododisciplina'


class Professor(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    ra = models.IntegerField()
    apelido = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'professor'
        unique_together = (('ra', 'apelido'),)


class Questao(models.Model):
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    numero = models.IntegerField()
    data_limite_entrega = models.CharField(max_length=10)
    descricao = models.TextField()  # This field type is a guess.
    datas = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'questao'


class Resposta(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='id_questao')
    data_avaliacao = models.CharField(max_length=10)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    avaliacao = models.TextField()  # This field type is a guess.
    descricao = models.TextField()  # This field type is a guess.
    data_de_envio = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'resposta'


class Turma(models.Model):
    id_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor')
    id_disciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='id_disciplinaofertada')
    turno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'turma'


class Usuario(models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)
    tipo_usuario = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'usuario'
