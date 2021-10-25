from functools import reduce
from typing import List

def is_substr(string: str, substring: str, case_sensitive: bool) -> bool:
    if case_sensitive:
        return string.find(substring) != -1

    return string.lower().find(substring.lower()) != -1


def avg(values: List[int], ndigits = 2) -> int:
    sum = reduce(lambda acc, v: acc + v, values)
    return round(sum / len(values), ndigits)

