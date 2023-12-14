import os
from django.http import Http404
from django.views.static import serve
from django.conf import settings
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
    
# Serve volume cover

def serve_volume_cover(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response
    
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
    
# Serve character picture
    
def serve_character_picture(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response