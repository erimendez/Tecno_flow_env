from rest_framework.serializers import ModelSerializer
from .models import Cotizacion

class CotizacionSerializer(ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = "__all__"