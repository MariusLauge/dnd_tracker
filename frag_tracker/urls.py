from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.CharacterListView.as_view(), name='characterlistview'),
    url(r'^character/(?P<pk>\d+)$', views.character_detail_view, name='character-detail'),
    url(r'^characterlistview', views.CharacterListView.as_view(), name='redirecthomepage'),
    url(r'^halloffame/$', views.hall_of_fame_list_view, name="halloffameview"),
]