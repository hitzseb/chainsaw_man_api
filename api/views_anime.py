from .serializers import AnimeSerializer, AnimeSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Anime

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