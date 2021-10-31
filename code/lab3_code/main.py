from functools import wraps

from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort
from lab_python_fp.print_task import print_task
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer1 import CmTimer
from lab_python_fp.cm_timer2 import cm_timer2

@print_task
def task1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print('Titles:')
    for good in field(goods, 'title'):
        print(good)

    print()

    print('Prices:')
    for good in field(goods, 'price'):
        print(good)

    print()

    print('Titles and prices:')
    for good in field(goods, 'title', 'price'):
        print(good)


@print_task
def task2():
    for r in gen_random(5, 1, 3):
        print(r)


@print_task
def task3():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('case sensitive:')
    for d in Unique(data):
        print(d)

    print('case insensitive:')
    for d in Unique(data, True):
        print(d)


@print_task
def task4():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    sort(data)

@print_task
def task5():
    @print_result
    def test_primitive_1():
        return 1


    @print_result
    def test_primitive_2():
        return 'iu5'


    @print_result
    def test_dictionary():
        return {'a': 1, 'b': 2}


    @print_result
    def test_list():
        return [1, 2]


    test_primitive_1()
    test_primitive_2()
    test_dictionary()
    test_list()

@print_task
def task6():
    num_of_iterations = 100_000_000
    def test_function():
        for i in range(num_of_iterations):
            continue

    print(f'{num_of_iterations:,.0f} iterations were completed in:')
    with CmTimer() as test_timer1:
        test_function()
    print('(class implementation)')
    print()

    with cm_timer2() as test_timer2:
        test_function()
    print('(contextlib @contextmanager decorator implementation)')



def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


if __name__ == "__main__":
    main()
