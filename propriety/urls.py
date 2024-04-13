from rest_framework import routers, urlpatterns

from .viewset import ProprietyViewSet

router = routers.SimpleRouter()
router.register('bienes_raices', ProprietyViewSet)

urlpatterns = router.urls