from typing import Iterator, Type
from task_decorator import task_decorator
from data import programming_languages, ides, programming_languages_ides
from models import ProgrammingLanguage, Ide
from _utilities import is_substr, avg

""" Selectors-generators. """
def select_programming_languages(subtitle = '', case_sensitive = False) -> Iterator[ProgrammingLanguage]:
    return (pl for pl in programming_languages if is_substr(pl.title, subtitle, case_sensitive))


def select_ides(programming_language_id: int) -> Iterator[Ide]:
    return (ide for ide in ides if ide.programming_language_id == programming_language_id)


@task_decorator(' Task #1. ')
def task1(programming_language_subtitle) -> None:
    print(f'Searching for \'{programming_language_subtitle}\' in language titles...')

    for pl in select_programming_languages(programming_language_subtitle, True):
        print(pl.title)
        print('IDEs available:')
        for ide in select_ides(pl.id):
            print(f'- {ide.to_string_formatted()}')

@task_decorator(' Task #2. ')
def task2() -> None:
    print('Mean IDE price...')
    for pl in select_programming_languages():
        output = f'- for {pl.title}: '

        prices = []
        for ide in select_ides(pl.id):
            prices.append(ide.price)

        output += str(avg(prices))
        print(output)


def select_ides_many_to_many(programming_language_id: int) -> Iterator[Ide]:
    return (ide
        for ide in ides
        for pli in programming_languages_ides
        if ide.id == pli.ide_id and programming_language_id == pli.programming_language_id)


@task_decorator(' Task #3. ')
def task3() -> None:
    print('IDEs starting from \'A\'')
    for pl in select_programming_languages():
        print(f'{pl.title}:')
        for ide in select_ides_many_to_many(pl.id):
            if (ide.title.startswith('A')):
                print(f'- {ide.to_string_formatted()}')


def main() -> None:
    task1('Ja')
    task2()
    task3()


if __name__ == "__main__":
    main()
