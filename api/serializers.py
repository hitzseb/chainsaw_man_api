from rest_framework import serializers
from .models import *

class SagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot']
        
class SagaSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ['number', 'title']
        
class ArcListSerializer(serializers.ModelSerializer):
    saga = SagaSerializerMin(many=False, read_only=True)
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
class ArcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
class ArcSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Arc
        fields = ['number', 'title']
        
class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'cover']
        
class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'picture']
        
class VolumeSerializer(serializers.ModelSerializer):
    manga = MangaListSerializer(many=True, read_only=True)
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'plot', 'cover', 'manga']
        
class VolumeSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['number', 'title', 'cover']
        
class MangaDetailSerializer(serializers.ModelSerializer):
    volume = VolumeSerializerMin(many=False, read_only=True)
    arc = ArcSerializerMin(many=False, read_only=True)
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc']
        
class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc']
        
class MangaSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'cover']
        
class CharacterDetailSerializer(serializers.ModelSerializer):
    manga_debut = MangaSerializerMin(many=False, read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'species', 'status', 'manga_debut']
        
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'species', 'status', 'manga_debut']