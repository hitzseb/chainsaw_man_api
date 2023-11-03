from django.urls import path
from .views import *

urlpatterns = [
    # saga urls
    path('sagas/list/', SagaListView.as_view(), name='saga-list'),
    path('sagas/create/', SagaCreateView.as_view(), name='saga-create'),
    path('sagas/rud/<int:number>/', SagaRetrieveUpdateDestroyView.as_view(), name='saga-rud'),
    # arc urls
    path('arcs/list/', ArcListView.as_view(), name='arc-list'),
    path('arcs/create/', ArcCreateView.as_view(), name='arc-create'),
    path('arcs/rud/<int:number>/', ArcRetrieveUpdateDestroyView.as_view(), name='arc-rud'),
    # volume urls
    path('volumes/list/', VolumeListView.as_view(), name='volume-list'),
    path('volumes/create/', VolumeCreateView.as_view(), name='volume-create'),
    path('volumes/rud/<int:number>/', VolumeRetrieveUpdateDestroyView.as_view(), name='volume-rud'),
    # manga urls
    path('manga/list/', MangaListView.as_view(), name='manga-list'),
    path('manga/detail/<int:number>/', MangaRetrieveView.as_view(), name='manga-retrieve'),
    path('manga/create/', MangaCreateView.as_view(), name='manga-create'),
    path('manga/rud/<int:number>/', MangaRetrieveUpdateDestroyView.as_view(), name='manga-rud'),
    # character urls
    path('characters/list/', CharacterListView.as_view(), name='character-list'),
    path('characters/detail/<str:name>/', CharacterRetrieveView.as_view(), name='character-retrieve'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/rud/<str:name>/', CharacterRetrieveUpdateDestroyView.as_view(), name='character-rud'),
]