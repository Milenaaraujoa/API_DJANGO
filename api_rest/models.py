from django.db import models
from datetime import datetime
from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class Turmas(models.Model):
    id_turma = models.IntegerField(primary_key=True)
    modalidade = models.CharField(max_length=50)
    horario = models.TimeField()
    dia_semana = models.CharField(max_length=20)
    faixa_etaria = models.CharField(max_length=20)
    

class Alunos(models.Model):
    cpf_alunos = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=12)
    cep = models.CharField(max_length=9, null=True)
    rua = models.CharField(max_length=200, null=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=2, null=True)
    numero = models.IntegerField( null=True)
    modalidade = models.CharField(max_length=50, null=True)
    turmas = models.CharField(max_length=50, null=True)
    
    
    def whatsapp_message_button(self):
        if not self.telefone:
            return "Telefone não disponível"
        
        # Remove caracteres não numéricos do telefone
        telefone_formatado = ''.join(filter(str.isdigit, self.telefone))
        telefone_formatado = f'55{telefone_formatado}' if len(telefone_formatado) <= 11 else telefone_formatado
        
        # Mensagem predefinida
        mensagem = f"Olá, {self.nome}! Estamos entrando em contato para informar sobre sua solicitação de matrícula."
        mensagem_codificada = mensagem.replace(" ", "%20")  # Substitui espaços por %20 para o link
        
        # Gera o link do WhatsApp
        link = f"https://wa.me/{telefone_formatado}?text={mensagem_codificada}"
        return format_html('<a href="{}" target="_blank" class="button">Enviar WhatsApp</a>', link)

    def __str__(self):
        return self.nome
    
    

class Evento(models.Model):
    nome_evento = models.CharField(max_length=100, primary_key=True)
    vagas = models.IntegerField()
    data_evento = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

class ContagemAlunos(models.Model):
    mes = models.CharField(max_length=7, unique=True)  # Ex: "2025-02"
    quantidade = models.IntegerField(default=0)