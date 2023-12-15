from .serializers import CharacterSerializer, CharacterSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Character

# Get all characters
class CharacterListView(ListAPIView):
    queryset = Character.objects.order_by('manga_debut__number')
    serializer_class = CharacterSerializerSm
    
# Get character by name
class CharacterRetrieveView(RetrieveAPIView):
    serializer_class = CharacterSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        name = self.kwargs['name']
        return Character.objects.filter(name=name)