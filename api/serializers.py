from pickle import OBJ
from rest_framework import serializers
from urllib.parse import quote
from core.models import *
from constants import SERVER_URL
import re

# Small serializers
# with partial data, used for nested serializers

class SagaSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Saga
        fields = ['number', 'title', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/saga/{obj.number}/')
        
class ArcSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Arc
        fields = ['number', 'title', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/arc/{obj.number}/')
        
class VolumeSerializerSm(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    class Meta:
        model = Volume
        fields = ['number', 'title', 'cover', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/volume/{obj.number}/')
    
    def get_cover(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/volume/cover/{obj.cover.name}')
        
class MangaSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Manga
        fields = ['number', 'title', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/manga/{obj.number}/')

class SeasonSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Season
        fields = ['number', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/season/{obj.number}/')
      
class AnimeSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/anime/{obj.number}/')
        
class SpeciesSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Species
        fields = ['name', 'url']
        
    def get_url(self, obj):
        request = self.context.get('request')
        encoded_name = quote(obj.name)
        return request.build_absolute_uri(f'/api/species/{encoded_name}/')
        
class CharacterSerializerSm(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = ['name', 'picture', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        encoded_name = quote(obj.name)
        return request.build_absolute_uri(f'/api/character/{encoded_name}/')

    def get_picture(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/character/picture/{obj.picture.name}')

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
        
    def get_cover(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/volume/cover/{obj.cover.name}')
        
class MangaSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()
    volume = VolumeSerializerSm(many=False, read_only=True)
    arc = ArcSerializerSm(many=False, read_only=True)
    characters = CharacterSerializerSm(many=True, read_only=True)
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'volume', 'arc', 'characters']
        
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
    picture = serializers.SerializerMethodField()
    species = SpeciesSerializerSm(many=False, read_only=True)
    manga_debut = MangaSerializerSm(many=False, read_only=True)
    anime_debut = AnimeSerializerSm(many=False, read_only=True)
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'status', 'species', 'manga_debut', 'anime_debut']
        
    def get_picture(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/character/picture/{obj.picture.name}')