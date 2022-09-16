#!/usr/bin/python3

import timeit
import sys
from functools import reduce

def loop_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

def reduce_sum(n):
    return reduce(lambda x, y: x + y ** 2, [i for i in range(1, n + 1)])

def compare_results(command, num, n):
    if command == 'loop':
        stmt_loop = f'loop_sum({n})'
        setup_loop = 'from __main__ import loop_sum'
        time = [timeit.timeit(stmt=stmt_loop, setup=setup_loop, number=num), 'loop']
    if command == 'reduce':
        stmt_reduce = f'reduce_sum({n})'
        setup_reduce = 'from __main__ import reduce_sum'
        time = [timeit.timeit(stmt=stmt_reduce, setup=setup_reduce, number=num), 'list comprehension']
    print(f'{time[0]}')

def main(argv):
    commands = ['loop', 'reduce']
    if len(argv) == 4 and argv[1] in commands:
        compare_results(argv[1], int(argv[2]), int(argv[3]))
    else:
        raise Exception("Arguments error. Usage: /benchmark.py <name of the function (loop, reduce)> <number of calls>")

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        print(e, file=sys.stderr)