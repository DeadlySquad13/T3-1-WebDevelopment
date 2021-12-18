from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Anime

def index(request):
    anime_instances = Anime.objects.all()

    # rated_animes_instances = { anime:get_anime_avg_score(anime) for anime in anime_instances }

    animes_sorted = sorted(anime_instances, key=lambda a: a.get_avg_score(), reverse=True)

    template = loader.get_template('anime/index.html')

    context = {
        'animes': animes_sorted
    }

    return HttpResponse(template.render(context, request))


def detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)

    context = {
        'anime': anime
    }

    return render(request, 'anime/detail.html', context)


def results(request, anime_id):
    response = f'You are looking at the results of anime {anime_id}'
    return HttpResponse(response)


def rate(request, anime_id):
    return HttpResponse(f'You are rating anime {anime_id}')

