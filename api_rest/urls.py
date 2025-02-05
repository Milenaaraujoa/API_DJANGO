
from django.contrib import admin
from django.urls import path, include

from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Alunos
    path('alunos/', views.AlunoListCreate.as_view(), name='aluno-list-create'),
    path('alunos/<str:cpf_alunos>/', views.AlunoRetrieveUpdateDestroy.as_view(), name='aluno-retrieve-update-destroy'),
    
    # Turmas
    path('turmas/', views.TurmaListCreate.as_view(), name='turma-list-create'),
    path('turmas/<int:id_turma>/', views.TurmaRetrieveUpdateDestroy.as_view(), name='turma-retrieve-update-destroy'),
    
    # Eventos
    path('eventos/', views.EventoListCreate.as_view(), name='evento-list-create'),
    path('eventos/<str:nome_evento>/', views.EventoRetrieveUpdateDestroy.as_view(), name='evento-retrieve-update-destroy'),
]