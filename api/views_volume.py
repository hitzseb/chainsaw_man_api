from .serializers import VolumeSerializer, VolumeSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Volume

# Get all volumes
class VolumeListView(ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializerSm
    
# Get volume by number
class VolumeRetrieveView(RetrieveAPIView):
    serializer_class = VolumeSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Volume.objects.filter(number=number)