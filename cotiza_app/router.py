from rest_framework import routers
from .viewsets import CotizacionViewSet

router = routers.SimpleRouter()
router.register("api-cotiza",CotizacionViewSet)