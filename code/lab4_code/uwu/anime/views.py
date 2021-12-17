from django.http import HttpResponse
from django.template import loader

from .models import Anime
from .utilities import avg


def get_avg_score(anime):
    anime_scores = anime.score_set.all()

    return avg([s.score for s in anime_scores])


def index(request):
    anime_list = Anime.objects.all()

    anime_list_sorted = sorted(anime_list, key=get_avg_score, reverse=True)

    template = loader.get_template('anime/index.html')

    context = {
        'anime_list': anime_list_sorted
    }

    return HttpResponse(template.render(context, request))


def detail(request, anime_id):
    return HttpResponse(f'You are looking at anime {anime_id}')


def results(request, anime_id):
    response = f'You are looking at the results of anime {anime_id}'
    return HttpResponse(response)


def rate(request, anime_id):
    return HttpResponse(f'You are rating anime {anime_id}')
