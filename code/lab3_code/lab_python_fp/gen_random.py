from random import randrange

def gen_random(num_count, begin, end):
    for i in range(num_count):
         # randrange works in [begin, end) diapason.
        yield randrange(begin, end + 1)

