from rest_framework import routers, urlpatterns
from django.urls import path
from .viewset import registrar_propiedad
from .viewset import editar_propiedad
from .viewset import eliminar_propiedad
from .viewset import listar_viviendas
from .viewset import ViviendaViewSet

router = routers.SimpleRouter()
router.register('bienes_raices', ViviendaViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('lista-de-empleados/', listar_viviendas, name='listar_viviendas'),
    path('registrar_propiedad/', registrar_propiedad, name='registrar_propiedad'),
    path('editar_propiedad/', editar_propiedad, name='editar_propiedad'),
    path('eliminar_propiedad/', eliminar_propiedad, name='eliminar_propiedad'),
    
]