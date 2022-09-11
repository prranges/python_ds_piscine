def read():
    with open('ds.csv', 'r') as input:
        with open('ds.tsv', 'w') as output:
            for line in input:
                output.write(line.replace('\",', '\"\t')
                                .replace('false,', 'false\t')
                                .replace('true,', 'true\t'))


if __name__ == '__main__':
    read()
