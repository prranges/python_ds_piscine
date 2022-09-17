#!/usr/bin/python3

import timeit
import random
from collections import Counter

def my_function(nums):
    counter = dict()
    for num in nums:
        if num not in counter:
            counter[num] = 1
        counter[num] += 1
    return counter

def my_top(nums):
    counter = my_function(nums)
    return sorted(counter.items(), key=lambda x: -x[1])[:10]

def compare_results(nums):
    setup = """
import random
from collections import Counter
from __main__ import my_function, my_top
random.seed(5)
"""

    stmt_my_function = f'my_function({nums})'
    my_function = timeit.timeit(stmt=stmt_my_function, setup=setup, number=1)
    stmt_counter = f'Counter({nums})'
    counter = timeit.timeit(stmt=stmt_counter, setup=setup, number=1)
    stmt_my_top = f'my_top({nums})'
    my_top = timeit.timeit(stmt=stmt_my_top, setup=setup, number=1)
    stmt_my_counter_top = f'Counter({nums}).most_common(10)'
    my_counter_top = timeit.timeit(setup=setup, stmt=stmt_my_counter_top, number=1)
    
    print(f"my function: {my_function}")
    print(f"Counter: {counter}")
    print(f"my top: {my_top}")
    print(f"Counter's top: {my_counter_top}")


if __name__ == '__main__':
    nums = [random.randint(0, 100) for i in range(1000000)]
    compare_results(nums)