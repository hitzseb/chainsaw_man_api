from .serializers import SpeciesSerializer, SpeciesSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Species

# Get all species
class SpeciesListView(ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializerSm
    
# Get species by name
class SpeciesRetrieveView(RetrieveAPIView):
    serializer_class = SpeciesSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        name = self.kwargs['name']
        return Species.objects.filter(name=name)