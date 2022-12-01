from time import time
from bowls import *


def time_func(func, n):
    t0 = time()
    print(f'Function called: {func}')
    print(f'Result: {func(n)}')
    t1 = time()
    elapsed = round((t1 - t0)*1000, 10)
    print(f'Took {elapsed}ms')

n = 10000000
time_func(sum_bowls_loop, n)
time_func(sum_bowls_loop_while, n)
#time_func(sum_bowls_recursive, n)
time_func(sum_bowls_seq, n)