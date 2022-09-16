#!/usr/bin/python3

import timeit
import sys

def loop_filter(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'): gmails.append(email)
    return gmails

def comprehension_filter(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def map_filter(emails):
    return map(lambda email: email if email.endswith('@gmail.com') else None, emails)

def filter_filter(emails):
    return filter(lambda email: email.endswith('@gmail.com'), emails)

def compare_results(command, num):
    emails = 5 * ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    if command == 'loop':
        stmt_loop = f'loop_filter({emails})'
        setup_loop = 'from __main__ import loop_filter'
        time = [timeit.timeit(stmt=stmt_loop, setup=setup_loop, number=num), 'loop']
    if command == 'list_comprehension':
        stmt_comp = f'comprehension_filter({emails})'
        setup_comp = 'from __main__ import comprehension_filter'
        time = [timeit.timeit(stmt=stmt_comp, setup=setup_comp, number=num), 'list comprehension']
    if command == 'map':
        stmt_map = f'map_filter({emails})'
        setup_map = 'from __main__ import map_filter'
        time = [timeit.timeit(stmt=stmt_map, setup=setup_map, number=num), 'map']
    if command == 'filter':
        stmt_filter = f'filter_filter({emails})'
        setup_filter = 'from __main__ import filter_filter'
        time = [timeit.timeit(stmt=stmt_filter, setup=setup_filter, number=num), 'filter']

    print(f'{time[0]}')

def main(argv):
    commands = ['loop', 'list_comprehension', 'map', 'filter']
    if len(argv) == 3 and argv[1] in commands:
        compare_results(argv[1], int(argv[2]))
    else:
        raise Exception("Arguments error. Usage: /benchmark.py <name of the function (loop, list_comprehension, map, filter)> <number of calls>")

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        print(e, file=sys.stderr)