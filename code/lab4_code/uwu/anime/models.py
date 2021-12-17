from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    poster = models.ImageField(blank=True)

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

