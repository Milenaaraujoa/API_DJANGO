from rest_framework import serializers

from .models import Alunos, Turmas, Evento
from rest_framework import serializers

from .models import Alunos, Turmas, Evento, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'

class AlunosSerializer(serializers.ModelSerializer):
    data_nascimento = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y", "%Y-%m-%d"])
    class Meta:
        model = Alunos
        fields = '__all__'

class TurmasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turmas
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    data_evento = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y", "%Y-%m-%d"])
    class Meta:
        model = Evento
        fields = '__all__'