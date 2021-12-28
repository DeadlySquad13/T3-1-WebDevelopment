from functools import reduce
from typing import List


def avg(values: List[int], ndigits = 2) -> int:
    sum = reduce(lambda acc, v: acc + v, values)
    return round(sum / len(values), ndigits)


def get_anime_avg_score(anime):
    anime_scores = anime.score_set.all()

    return 0 if not anime_scores else avg([s.score for s in anime_scores])

