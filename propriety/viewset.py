from rest_framework import viewsets, Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Login, ProprietyVivienda
from .serializer import LoginSerializer, ViviendaSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = ProprietyVivienda.objects.all
    serializer_class = ViviendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo']

class ViviendaList(viewsets.ModelViewSet):
    def list(self, request):
        #id de la vivienda
        idViviendaVar = request.query_params.get('idVivienda')
        queryset = ProprietyVivienda.objects.filter()
        serializer_class =  ViviendaSerializer(queryset, many=True)
        return Response(serializer_class)