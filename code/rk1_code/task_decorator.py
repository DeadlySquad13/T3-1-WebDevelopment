from functools import wraps

""" Decorating output of a task. """
def task_decorator(output):
    def decorator(wrapped_function):
        @wraps(wrapped_function)
        def wrapper(*args, **kwargs):
            print(f'----------------------{output}----------------------')
            wrapped_function(*args, **kwargs);
            print()

        return wrapper

    return decorator
