from rest_framework import generics
from .models import Alunos, Turmas, Evento, User
from .serializers import AlunosSerializer, TurmasSerializer, EventoSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


#View para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Views para Alunos
class AlunoListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class AlunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

# Views para Turmas
class TurmaListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

class TurmaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Turma alterada com sucesso!'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Turma deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

# Views para Eventos
class EventoListCreate(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    

class EventoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Evento alterado com sucesso!'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Evento deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)