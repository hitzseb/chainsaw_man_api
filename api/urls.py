from django.urls import path
from .views import *

urlpatterns = [
    path('saga/', SagaListView.as_view(), name='saga_list_drf'),
    path('saga/<int:number>/', SagaRetrieveView.as_view(), name='saga_detail_drf'),
    path('arc/', ArcListView.as_view(), name='arc_list_drf'),
    path('arc/<int:number>/', ArcRetrieveView.as_view(), name='arc_detail_drf'),
    path('volume/', VolumeListView.as_view(), name='volume_list_drf'),
    path('volume/<int:number>/', VolumeRetrieveView.as_view(), name='volume_detail_drf'),
    path('volume/cover/<str:image_filename>/', serve_volume_cover, name='serve_volume_cover'),
    path('manga/', MangaListView.as_view(), name='manga_list_drf'),
    path('manga/<int:number>/', MangaRetrieveView.as_view(), name='manga_detail_drf'),
    path('season/', SeasonListView.as_view(), name='season_list_drf'),
    path('season/<int:number>/', SeasonRetrieveView.as_view(), name='season_detail_drf'),
    path('anime/', AnimeListView.as_view(), name='anime_list_drf'),
    path('anime/<str:number>/', AnimeRetrieveView.as_view(), name='anime_detail_drf'),
    path('character/', CharacterListView.as_view(), name='character_list_drf'),
    path('character/<str:name>/', CharacterRetrieveView.as_view(), name='character_detail_drf'),
    path('character/picture/<str:image_filename>/', serve_character_picture, name='serve_character_picture'),
    path('species/', SpeciesListView.as_view(), name='species_list_drf'),
    path('species/<str:name>/', SpeciesRetrieveView.as_view(), name='species_detail_drf'),
]