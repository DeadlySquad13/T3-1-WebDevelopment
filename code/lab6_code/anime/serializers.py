from .models import Anime, Score
from rest_framework import serializers


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['title', 'description', 'poster']


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ['anime', 'score']
        
