from django.shortcuts import render
from django.views import generic
from .models import Character
from django.http import Http404


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


def character_detail_view(request, pk):
    try:
        character_id = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        raise Http404("Book does not exist")

    return render(
        request,
        'frag_tracker/character_detail.html',
        context={'character': character_id, }
    )

class HallOfFameListView(generic.ListView):
    model = Character

    context_object_name = 'hall_of_fame_list'
    template_name = 'frag_tracker/templates/frag_tracker/hall_of_fame.html'