from django.contrib import admin

from .models import Alunos, Turmas, Evento

admin.site.register(Alunos)
admin.site.register(Turmas)
admin.site.register(Evento)