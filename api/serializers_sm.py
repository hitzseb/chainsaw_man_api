from rest_framework import serializers
from urllib.parse import quote
from core.models import *

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
        return request.build_absolute_uri(f'/api/volume/cover/{obj.cover.name}/')
        
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
        return request.build_absolute_uri(f'/api/character/picture/{obj.picture.name}/')