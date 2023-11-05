from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from utils import is_admin

# Saga views

class SagaListView(ListAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class SagaCreateView(CreateAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class SagaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer
    lookup_field = 'number'
    
# Arc views

class ArcListView(ListAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcListSerializer
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArcCreateView(CreateAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArcRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer
    lookup_field = 'number'
    
# Volume views

class VolumeListView(ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class VolumeCreateView(CreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class VolumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    lookup_field = 'number'
    
# Manga views

class MangaListView(ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    
class MangaRetrieveView(RetrieveAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer
    lookup_field = 'number'
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MangaCreateView(CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class MangaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'number'
    
# Character views

class CharacterListView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    
class CharacterRetrieveView(RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_field = 'name'
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class CharacterCreateView(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class CharacterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'name'