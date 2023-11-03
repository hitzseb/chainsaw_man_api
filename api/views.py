from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from rest_framework import generics
from .serializers import *
from .models import *

def is_admin(user):
    return user.is_authenticated and user.is_staff

# Saga views

class SagaListView(generics.ListAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class SagaCreateView(generics.CreateAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class SagaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saga.objects.all()
    serializer_class = SagaSerializer
    lookup_field = 'number'
    
# Arc views

class ArcListView(generics.ListAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArcCreateView(generics.CreateAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class ArcRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arc.objects.all()
    serializer_class = ArcSerializer
    lookup_field = 'number'
    
# Volume views

class VolumeListView(generics.ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class VolumeCreateView(generics.CreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class VolumeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    lookup_field = 'number'
    
# Manga views

class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    
class MangaRetrieveView(generics.RetrieveAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer
    lookup_field = 'number'
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class MangaCreateView(generics.CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class MangaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer
    lookup_field = 'number'
    
# Character views

class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    
class CharacterRetrieveView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_field = 'name'
    
@method_decorator(user_passes_test(is_admin), name='dispatch')
class CharacterCreateView(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer

@method_decorator(user_passes_test(is_admin), name='dispatch')
class CharacterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    lookup_field = 'name'