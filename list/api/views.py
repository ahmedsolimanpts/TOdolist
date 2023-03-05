from rest_framework.viewsets import ModelViewSet
from ..models import List
from .serializers import ListSerializers
class TODOList(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializers