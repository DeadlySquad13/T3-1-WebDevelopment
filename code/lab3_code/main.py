from functools import wraps

from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random

def beginning_decorator(output):
    def decorator(wrapped_function):
        @wraps(wrapped_function)
        def wrapper():
            print(f'-----{output}-----')
            wrapped_function();
            print()

        return wrapper

    return decorator

@beginning_decorator('Task #1')
def task1_test():
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

    print()


@beginning_decorator('Task #2')
def task2_test():
    for r in gen_random(5, 1, 3):
        print(r)


def main() -> None:
    task1_test()
    task2_test()


if __name__ == "__main__":
    main()
