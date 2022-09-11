from email.quoprimime import quote


def data_types():
    types = [1, '1', 1.0, True, [], {}, (1,), {1}]

    print(str([type(t).__name__ for t in types]).replace("'", ""))


if __name__ == '__main__':
    data_types()