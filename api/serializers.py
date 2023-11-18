from rest_framework import serializers
from core.models import *

# Small serializers

class SagaSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ['number', 'title']
        
class ArcSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Arc
        fields = ['number', 'title']   
        
class VolumeSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['number', 'title', 'cover']
        
class MangaSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'cover'] 

class SeasonSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['number']
      
class AnimeSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date']
        
class SpeciesSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['name']
        
class CharacterSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'picture']

# Full serializers

class SagaSerializer(serializers.ModelSerializer):
    arcs = ArcSerializerSm(many=True, read_only=True)
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot', 'arcs']
        
class ArcSerializer(serializers.ModelSerializer):
    saga = SagaSerializerSm(many=False, read_only=True)
    chapters = MangaSerializerSm(many=True, read_only=True)
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga', 'chapters']
        
class VolumeSerializer(serializers.ModelSerializer):
    chapters = MangaSerializerSm(many=True, read_only=True)
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'plot', 'cover', 'chapters']
        
class MangaSerializer(serializers.ModelSerializer):
    volume = VolumeSerializerSm(many=False, read_only=True)
    arc = ArcSerializerSm(many=False, read_only=True)
    characters = CharacterSerializerSm(many=True, read_only=True)
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc', 'characters']
        
class SeasonSerializer(serializers.ModelSerializer):
    episodes = AnimeSerializerSm(many=True, read_only=True)
    class Meta:
        model = Season
        fields = ['number', 'plot', 'start_date', 'end_date', 'episodes']
        
class AnimeSerializer(serializers.ModelSerializer):
    season = SeasonSerializerSm(many=False, read_only=True)
    characters = CharacterSerializerSm(many=True, read_only=True)
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'plot', 'season', 'characters']
        
class SpeciesSerializer(serializers.ModelSerializer):
    characters = CharacterSerializerSm(many=True, read_only=True)
    class Meta:
        model = Species
        fields = ['name', 'description', 'characters']
        
class CharacterSerializer(serializers.ModelSerializer):
    species = SpeciesSerializerSm(many=False, read_only=True)
    manga_debut = MangaSerializerSm(many=False, read_only=True)
    anime_debut = AnimeSerializerSm(many=False, read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'status', 'species', 'manga_debut', 'anime_debut']