from contextlib import contextmanager
from time import time

@contextmanager
def cm_timer2():
    start_time = time()
    yield 333
    print(time() - start_time)

