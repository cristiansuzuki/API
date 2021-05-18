from django.contrib import admin
from escola.models import Aluno
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields_ = ('nome',)

admin.site.register(Aluno, Alunos)

