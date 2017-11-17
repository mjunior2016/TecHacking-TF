from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from core.models import *

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    pass

class AdminAluno(admin.ModelAdmin):
    pass

class AdminCurso(ModelAdmin):
    pass

class AdminTurma(ModelAdmin):
    pass

class AdminProfessor(ModelAdmin):
    pass

class AdminUsuario(ModelAdmin):
    pass

class AdminDisciplina(ModelAdmin):
    pass

class AdminDisciplinaOfertada(ModelAdmin):
    pass

class AdminMatricula(ModelAdmin):
    pass

admin.site.register(Turma, AdminTurma),
admin.site.register(Curso, AdminCurso),
admin.site.register(Aluno, AdminAluno),
admin.site.register(Professor, AdminProfessor),
admin.site.register(Usuario, AdminUsuario),
admin.site.register(Disciplina, AdminDisciplina),
admin.site.register(Disciplinaofertada,AdminDisciplinaOfertada)
admin.site.register(Matricula, AdminMatricula)