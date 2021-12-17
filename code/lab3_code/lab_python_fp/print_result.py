from functools import wraps
from types import GeneratorType as Generator

def print_result(function_to_wrap):
    @wraps(function_to_wrap)
    def wrapper(*args, **kwargs):
        print(function_to_wrap.__name__)
        result = function_to_wrap(*args, **kwargs)
        if isinstance(result, list) or isinstance(result, Generator):
            for item in result:
                print(item)

            return result

        if isinstance(result, dict):
            for key, item in result.items():
                print(f'{key} = {item}')

            return result

        print(result)
        return result

    return wrapper

