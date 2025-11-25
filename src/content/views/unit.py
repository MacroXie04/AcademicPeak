from rest_framework import viewsets
from content.models import Unit
from content.serializers import UnitSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

