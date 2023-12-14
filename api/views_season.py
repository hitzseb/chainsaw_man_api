from .serializers import SeasonSerializer, SeasonSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Season

# Get all seasons
class SeasonListView(ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializerSm
    
# Get season by number
class SeasonRetrieveView(RetrieveAPIView):
    serializer_class = SeasonSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Season.objects.filter(number=number)