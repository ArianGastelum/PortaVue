from rest_framework import routers

from .viewset import LoginViewSet

router = routers.SimpleRouter()
router.register('login', LoginViewSet)

urlpatterns = router.urls