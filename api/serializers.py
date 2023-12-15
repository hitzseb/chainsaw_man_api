from rest_framework import serializers
from .serializers_sm import *
from core.models import *

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
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'cover', 'plot', 'chapters']
        
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
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc', 'characters']
        
    def get_cover(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/volume/cover/{obj.cover.name}')
        
class SeasonSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    episodes = AnimeSerializerSm(many=True, read_only=True)
    class Meta:
        model = Season
        fields = ['number',  'poster','start_date', 'end_date', 'plot','episodes']
        
    def get_poster(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/season/poster/{obj.poster.name}/')
        
class AnimeSerializer(serializers.ModelSerializer):
    still = serializers.SerializerMethodField()
    season = SeasonSerializerSm(many=False, read_only=True)
    characters = CharacterSerializerSm(many=True, read_only=True)
    class Meta:
        model = Anime
        fields = ['number', 'title', 'still', 'date', 'plot', 'season', 'characters']
        
    def get_still(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/anime/still/{obj.still.name}/')
        
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