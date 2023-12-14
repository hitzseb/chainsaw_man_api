from .serializers import MangaSerializer, MangaSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Manga

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