from django.db import models
from .utilities import avg


class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    poster = models.ImageField(upload_to='./', blank=True)

    def get_avg_score(self):
        anime_scores = self.score_set.all()

        return 0 if not anime_scores else avg([s.score for s in anime_scores])

    def __str__(self):
        return (
            f'Title: {self.title}.\n'
            f'Description: {self.description}'
        )


class Score(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.anime.title}: {self.score}'

