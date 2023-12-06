from rest_framework import serializers
from urllib.parse import quote
from core.models import *

# Small serializers
# with partial data, used for nested serializers

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
    url = serializers.SerializerMethodField()
    class Meta:
        model = Manga
        fields = ['number', 'title', 'cover', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/manga/{obj.number}/')

class SeasonSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['number']
      
class AnimeSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/anime/{obj.number}/')
        
class SpeciesSerializerSm(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['name']
        
class CharacterSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Character
        fields = ['name', 'picture', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        encoded_name = quote(obj.name)
        return request.build_absolute_uri(f'/api/character/{encoded_name}/')

# Full serializers
# with complete data, used for main serializers

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
        fields = ['number', 'title', 'date', 'cover', 'volume', 'arc', 'characters']
        
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
        fields = ['number', 'title', 'date', 'season', 'characters']
        
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