from .models import Anime, Score
from rest_framework import viewsets
from .serializers import AnimeSerializer, ScoreSerializer


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

