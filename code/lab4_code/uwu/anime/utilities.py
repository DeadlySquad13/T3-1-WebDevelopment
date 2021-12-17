from functools import reduce
from typing import List


def avg(values: List[int], ndigits = 2) -> int:
    sum = reduce(lambda acc, v: acc + v, values)
    return round(sum / len(values), ndigits)

