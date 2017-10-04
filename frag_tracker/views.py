from django.shortcuts import render
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