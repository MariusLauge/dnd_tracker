from django.shortcuts import render
from django.views import generic
from .models import Character


def index(request):
    """
    Home page for the site.    
    """
    num_characters = Character.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_characters':num_characters}
    )


class CharacterListView(generic.ListView):
    model = Character

    context_object_name = 'character_list'
    template_name = 'frag_tracker/templates/frag_tracker/character_list.html'


class CharacterDetailView(generic.DetailView):
    model = Character