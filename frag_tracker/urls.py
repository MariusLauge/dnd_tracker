from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CharacterListView.as_view(), name='characterlistview'),
    url(r'^character/(?P<pk>\d+)$', views.CharacterDetailView.as_view(), name='character-detail'),
]