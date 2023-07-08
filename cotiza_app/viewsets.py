from rest_framework.viewsets import ModelViewSet
from .models import Cotizacion
from .serializers import CotizacionSerializer

class CotizacionViewSet(ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer