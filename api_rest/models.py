from django.db import models

from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank = True,      
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank = True,      
    )


class Alunos(models.Model):
    cpf_alunos = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=25)
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
            return "Telefone nÃ£o disponÃ­vel"
        
        # Remove caracteres nÃ£o numÃ©ricos do telefone
        telefone_formatado = ''.join(filter(str.isdigit, self.telefone))
        telefone_formatado = f'55{telefone_formatado}' if len(telefone_formatado) <= 11 else telefone_formatado
        
        # Mensagem predefinida
        mensagem = f"OlÃ¡, {self.nome}! Estamos entrando em contato para informar sobre sua solicitaÃ§Ã£o de matrÃ­cula."
        mensagem_codificada = mensagem.replace(" ", "%20")  # Substitui espaÃ§os por %20 para o link
        
        # Gera o link do WhatsApp
        link = f"https://wa.me/{telefone_formatado}?text={mensagem_codificada}"
        return format_html('<a href="{}" target="_blank" class="button">Enviar WhatsApp</a>', link)

    def __str__(self):
        return self.nome
    
class Turmas(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField(max_length=100, null = True)
    modalidade = models.CharField(max_length=50)
    horario = models.CharField(max_length=20)
    dia_semana = models.CharField(max_length=20)
    faixa_etaria = models.CharField(max_length=20)
    

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome_evento = models.CharField(max_length=100)
    vagas = models.IntegerField()
    data_evento = models.DateField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)