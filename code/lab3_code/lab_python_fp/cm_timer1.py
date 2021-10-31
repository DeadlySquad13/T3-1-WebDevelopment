from time import time

class CmTimer:
    def __init__(self):
        self._start_time = None

    def __enter__(self):
        self._start_time = time()
        return
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('-------------------')
            print(time() - self._start_time)
            print('-------------------')

