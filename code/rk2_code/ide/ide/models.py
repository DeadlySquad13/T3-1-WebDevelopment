from django.db import models


class ProgrammingLanguage(models.Model):
    """Язык программирования. """
    title = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.title}'


class Ide(models.Model):
    """Средство разработки. """
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)

    def __str__(self):
        return (
            f'Title: {self.title}, '
            f'price: {self.price if self.price != 0 else f"{self.price} (free)"}, '
            f'programming languages: {list(self.programming_languages.all())}'
        )

