def f():
    list_of_tuples = [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
    ]

    dict_of_tuples = {}
    for t in list_of_tuples:
        dict_of_tuples[t[1]] = t[0]
    
    for d in dict_of_tuples:
        print(d, ':', dict_of_tuples[d])


if __name__ == '__main__':
    f()