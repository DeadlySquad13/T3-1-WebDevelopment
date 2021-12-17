from django.http import HttpResponse

from .models import Anime


def index(request):
    anime_list = Anime.objects.all()
    anime_scores = [a.score_set.all() for a in anime_list]
    output = ', '.join([str(s) for s in anime_scores])
    return HttpResponse(output)


def detail(request, anime_id):
    return HttpResponse(f'You are looking at anime {anime_id}')


def results(request, anime_id):
    response = f'You are looking at the results of anime {anime_id}'
    return HttpResponse(response)


def rate(request, anime_id):
    return HttpResponse(f'You are rating anime {anime_id}')
