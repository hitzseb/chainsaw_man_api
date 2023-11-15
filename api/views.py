from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *

# Get all sagas
class SagaListView(ListAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

# Get all arcs
class ArcListView(ListAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer
    
# Get all volumes
class VolumeListView(ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    
# Get manga by number
class MangaRetrieveView(RetrieveAPIView):
    serializer_class = MangaSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Manga.objects.filter(number=number)
    
# Get all seasons
class SeasonListView(ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    
# Get anime by number
class AnimeRetrieveView(RetrieveAPIView):
    serializer_class = AnimeSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Anime.objects.filter(number=number)
    
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
    
# Get all characters
class CharacterListView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializerSm
    
# Get character by name
class CharacterRetrieveView(RetrieveAPIView):
    serializer_class = CharacterSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        name = self.kwargs['name']
        return Character.objects.filter(name=name)