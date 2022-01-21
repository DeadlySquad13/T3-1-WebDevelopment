from .models import Anime, Score, Status, Interest
from rest_framework import serializers


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['title', 'description', 'poster', 'status', 'interest']


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ['anime', 'score']


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['name', 'score']


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = ['name', 'score']

