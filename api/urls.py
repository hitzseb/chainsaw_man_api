from django.urls import path
from .views import *

urlpatterns = [
    path('saga/', SagaListView.as_view(), name='saga_list_drf'),
    path('arc/', ArcListView.as_view(), name='arc_list_drf'),
    path('volume/', VolumeListView.as_view(), name='volume_list_drf'),
    path('manga/<int:number>/', MangaRetrieveView.as_view(), name='manga_detail_drf'),
    path('season/', SeasonListView.as_view(), name='season_list_drf'),
    path('anime/<str:number>/', AnimeRetrieveView.as_view(), name='anime_detail_drf'),
    path('character/', CharacterListView.as_view(), name='character_list_drf'),
    path('character/<str:name>/', CharacterRetrieveView.as_view(), name='character_detail_drf'),
    path('species/', SpeciesListView.as_view(), name='species_list_drf'),
    path('species/<str:name>/', SpeciesRetrieveView.as_view(), name='species_detail_drf'),
]