from rest_framework import viewsets

from .models import Login, ProprietyVivienda
from .serializer import LoginSerializer, ProprietySerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ProprietyViewSet(viewsets.ModelViewSet):
    queryset = ProprietyVivienda.objects.all
    serializer_class = ProprietySerializer