from django.http import HttpResponse
from django.views import generic

from .models import Anime


class IndexView(generic.ListView):
    template_name = 'anime/index.html'
    context_object_name = 'animes'

    def get_queryset(self):
        anime_instances = Anime.objects.all()

        animes_sorted = sorted(
            anime_instances,
            key=lambda a: a.get_avg_score(),
            reverse=True
        )

        return animes_sorted


class DetailView(generic.DetailView):
    model = Anime
    template_name = 'anime/detail.html'


def rate(request, anime_id):
    return HttpResponse(f'You are rating anime {anime_id}')

