from functools import reduce
from multiprocessing import Pool
import time

def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

def measure(func):

    def inner(*kargs, **kwargs):
        start = time.process_time_ns()
        ret = func(*kargs, **kwargs)
        end = time.process_time_ns()
        print(f'time was {end-start}')
        return ret
    
    return inner

@measure
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

print(measure_me(100))