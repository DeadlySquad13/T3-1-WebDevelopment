from contextlib import contextmanager
from time import time

@contextmanager
def cm_timer2():
    start_time = time()
    yield
    print('-------------------')
    print(time() - start_time)
    print('-------------------')

