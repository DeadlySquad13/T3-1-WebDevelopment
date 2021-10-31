from functools import wraps

def print_task(function_to_wrap):
    @wraps(function_to_wrap)
    def wrapper(*args, **kwargs):
        print(f'------------- {function_to_wrap.__name__} -------------')
        function_to_wrap(*args, **kwargs);
        print()

    return wrapper

