from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *

# Get all sagas
class SagaListView(ListAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializerSm
    
# Get saga by number
class SagaRetrieveView(RetrieveAPIView):
    serializer_class = SagaSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Saga.objects.filter(number=number)

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
    
# Get all manga
class MangaListView(ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializerSm
    
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
    serializer_class = SeasonSerializerSm
    
# Get manga by number
class SeasonRetrieveView(RetrieveAPIView):
    serializer_class = SeasonSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Season.objects.filter(number=number)
    
# Get all anime
class AnimeListView(ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializerSm
    
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