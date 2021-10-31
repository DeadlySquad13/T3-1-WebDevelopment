from json import load
from lab_python_fp.print_result import print_result
from lab_python_fp.unique import Unique
from lab_python_fp.field import field
from lab_python_fp.cm_timer2 import cm_timer2
from lab_python_fp.gen_random import gen_random

@print_result
def f1(data):
    return sorted(Unique(field(data, 'job-name'), True), key=str.lower)


@print_result
def f2(vacancies):
    return list(filter(lambda v: v.lower().startswith('программист'), vacancies))

@print_result
def f3(programmers):
    return list(map(lambda programmer: f'{programmer} с опытом Python', programmers))

@print_result
def f4(vacancies):
    salaries = list(gen_random(len(vacancies), 100_000, 200_000))
    return list(map(lambda v: f'{v[0]}, запрлата {v[1]} руб.', zip(vacancies, salaries)))

def process_data(path) -> None:
    with open(path, encoding='utf8') as f:
        data = load(f)
    with cm_timer2() as process_data_timer:
        f4(f3(f2(f1(data))))
