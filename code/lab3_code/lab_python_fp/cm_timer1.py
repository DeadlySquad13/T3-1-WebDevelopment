from time import time

class CmTimer:
    def __init__(self):
        self._start_time = None
        pass 

    def __enter__(self):
        self._start_time = time()
        return 333
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(time() - self._start_time)

