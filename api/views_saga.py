from .serializers import SagaSerializer, SagaSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Saga

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