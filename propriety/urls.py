from rest_framework import routers, urlpatterns

from .viewset import ViviendaViewSet

router = routers.SimpleRouter()
router.register('bienes_raices', ViviendaViewSet)

urlpatterns = router.urls