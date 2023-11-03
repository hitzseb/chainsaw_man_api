from django.urls import path
from .views import *

urlpatterns = [
    # saga urls
    path('saga/', SagaListView.as_view(), name='saga-list'),
    path('saga/create', SagaCreateView.as_view(), name='saga-create'),
    path('saga/rud/<int:number>/', SagaRetrieveUpdateDestroyView.as_view(), name='saga-rud'),
    # arc urls
    path('arc/', ArcListView.as_view(), name='arc-list'),
    path('arc/create', ArcCreateView.as_view(), name='arc-create'),
    path('arc/rud/<int:number>/', ArcRetrieveUpdateDestroyView.as_view(), name='arc-rud'),
    # volume urls
    path('volume/', VolumeListView.as_view(), name='volume-list'),
    path('volume/create', VolumeCreateView.as_view(), name='volume-create'),
    path('volume/rud/<int:number>/', VolumeRetrieveUpdateDestroyView.as_view(), name='volume-rud'),
    # manga urls
    path('manga/', MangaListView.as_view(), name='manga-list'),
    path('manga/detail/<int:number>/', MangaRetrieveView.as_view(), name='manga-retrieve'),
    path('manga/create', MangaCreateView.as_view(), name='manga-create'),
    path('manga/rud/<int:number>/', MangaRetrieveUpdateDestroyView.as_view(), name='manga-rud'),
    # character urls
    path('character/', CharacterListView.as_view(), name='character-list'),
    path('character/detail/<str:name>/', CharacterRetrieveView.as_view(), name='character-retrieve'),
    path('character/create', CharacterCreateView.as_view(), name='character-create'),
    path('character/rud/<str:name>/', CharacterRetrieveUpdateDestroyView.as_view(), name='character-rud'),
]