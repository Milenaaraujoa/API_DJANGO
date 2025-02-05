from rest_framework import generics
from .models import Alunos, Turmas, Evento



from .serializers import AlunosSerializer, TurmasSerializer, EventoSerializer

# Views para Alunos
class AlunoListCreate(generics.ListCreateAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class AlunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

# Views para Turmas
class TurmaListCreate(generics.ListCreateAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

class TurmaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

# Views para Eventos
class EventoListCreate(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
