#from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from __future__ import unicode_literals

from django.db import models

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    ra = models.IntegerField(unique=True)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=80)

    class Meta:
        managed = True
        db_table = 'aluno'


class Arquivoquestao(models.Model):
    id = models.IntegerField(primary_key=True)
    id_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_questao', blank=True, null=True)
    arquivo_questao = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = True
        db_table = 'arquivoquestao'


class Arquivosresposta(models.Model):
    id = models.IntegerField(primary_key=True)
    id_resposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='id_resposta', blank=True, null=True)
    arquivos_resposta = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = True
        db_table = 'arquivosresposta'


class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'curso'
        unique_together = (('sigla', 'nome'),)


class Cursoturma(models.Model):
    id = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cursoturma'


class Disciplina(models.Model):
    id = models.IntegerField(primary_key=True)
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
        managed = True
        db_table = 'disciplina'


class Disciplinaofertada(models.Model):
    id = models.IntegerField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina', blank=True, null=True)
    nome_disciplina = models.CharField(max_length=240)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'disciplinaofertada'
        unique_together = (('nome_disciplina', 'ano', 'semestre'),)


class Gradecurricular(models.Model):
    id = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    ano = models.SmallIntegerField()
    semestre = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'gradecurricular'
        unique_together = (('ano', 'semestre'),)


class Matricula(models.Model):
    id = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'matricula'


class Periodo(models.Model):
    id = models.IntegerField(primary_key=True)
    id_gradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='id_gradecurricular', blank=True, null=True)
    numero = models.SmallIntegerField(unique=True)

    class Meta:
        managed = True
        db_table = 'periodo'


class Periododisciplina(models.Model):
    id = models.IntegerField(primary_key=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo', blank=True, null=True)
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'periododisciplina'


class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    ra = models.IntegerField(blank=True, null=True)
    apelido = models.CharField(max_length=30)
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'professor'
        unique_together = (('ra', 'apelido'),)


class Questao(models.Model):
    id = models.IntegerField(primary_key=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)
    numero = models.IntegerField(unique=True)
    data_limite_entrega = models.CharField(max_length=10)
    descricao = models.TextField()  # This field type is a guess.
    datas = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'questao'


class Resposta(models.Model):
    id = models.IntegerField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno', blank=True, null=True)
    id_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='id_questao', blank=True, null=True)
    ra_aluno = models.IntegerField(unique=True)
    data_avaliacao = models.CharField(max_length=10)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    avaliacao = models.TextField()  # This field type is a guess.
    descricao = models.TextField()  # This field type is a guess.
    data_de_envio = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'resposta'


class Turma(models.Model):
    id = models.IntegerField(primary_key=True)
    id_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor', blank=True, null=True)
    id_disciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='id_disciplinaofertada', blank=True, null=True)
    turno = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'turma'
