from rest_framework.viewsets import ModelViewSet
from ..models import Tasks
from .serializers import ListSerializers
class TODOList(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = ListSerializers