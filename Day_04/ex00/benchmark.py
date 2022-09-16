import timeit

def loop_filter(emails):
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'): gmails.append(email)
    return gmails

def comprehension_filter(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def compare_results(emails):
    num = 90000000
    stmt_loop = f'loop_filter({emails})'
    setup_loop = 'from __main__ import loop_filter'
    stmt_comp = f'comprehension_filter({emails})'
    setup_comp = 'from __main__ import comprehension_filter'
    loop = timeit.timeit(stmt=stmt_loop, setup=setup_loop, number=num)
    comp = timeit.timeit(stmt=stmt_comp, setup=setup_comp, number=num)
    res = 'loop' if loop < comp else 'list comprehension'
    print(f'it is better to use a {res}')
    time = sorted([loop, comp])
    print(f'{time[0]} vs {time[1]}')

if __name__ == '__main__':
    emails = 5 * ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    compare_results(emails)