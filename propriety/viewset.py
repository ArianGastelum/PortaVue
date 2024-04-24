from rest_framework import viewsets, response
from django_filters.rest_framework import DjangoFilterBackend

from .models import viviendas
from .serializer import ViviendaSerializer

class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = viviendas.objects.all
    serializer_class = ViviendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo']

class ViviendaList(viewsets.ModelViewSet):
    def list(self, request):
        #id de la vivienda
        idViviendaVar = request.query_params.get('idVivienda')
        queryset = viviendas.objects.filter()
        serializer_class =  ViviendaSerializer(queryset, many=True)
        return response(serializer_class)