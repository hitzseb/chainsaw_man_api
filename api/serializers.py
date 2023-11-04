from rest_framework import serializers
from .models import *

class SagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot']
        
class ArcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
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
        fields = ['number', 'date', 'cover', 'manga']
        
class MangaDetailSerializer(serializers.ModelSerializer):
    characters = CharacterListSerializer(many=True, read_only=True)
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc', 'characters']
        
class CharacterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'species', 'status', 'manga_debut']