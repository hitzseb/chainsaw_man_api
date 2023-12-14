from .serializers import ArcSerializer, ArcSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Arc

# Get all arcs
class ArcListView(ListAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializerSm
    
# Get arc by number
class ArcRetrieveView(RetrieveAPIView):
    serializer_class = ArcSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Arc.objects.filter(number=number)