from django.db import models

from .utilities import avg


# Status of the anime.
class Status(models.Model):
    name = models.CharField(max_length=20)
    # How much this status affects planning.
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.score})'


# Interest of user who plans to watch the anime.
class Interest(models.Model):
    name = models.CharField(max_length=20)
    # How much is user interested in watching this anime (how much affects
    #   planning).
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.score})'


class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    poster = models.ImageField(upload_to='./', blank=True)

    status = models.ForeignKey(Status, blank=True, on_delete=models.SET_NULL,
                               null=True)
    interest = models.ForeignKey(Interest, blank=True,
                                 on_delete=models.SET_NULL, null=True)

    def get_avg_score(self):
        anime_scores = self.score_set.all()

        return 0 if not anime_scores else avg([s.score for s in anime_scores])

    def __str__(self):
        return (
            f'Title: {self.title}\n'
            f'Description: {self.description}\n'
            f'Status: {self.status}'
        )


class Score(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.anime.title}: {self.score}'

