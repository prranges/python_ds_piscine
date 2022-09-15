import sys
import os

class Research:
    def __init__(self, file):
        self.file = file
        self.calculator = self.Calculations()

    def file_reader(self, has_header=True):
        if len(sys.argv) != 2:
            raise Exception('To many arguments.')
        if len(self.file.split('.')) != 2:
            raise Exception('Wrong file name.')
        with open(self.file, 'r') as input:
            lines = input.readlines()
        if lines[0].strip() == '0,1' or lines[0].strip() == '1,0':
            has_header = False
        if has_header:
            if len(lines[0].split(',')) != 2:
                raise Exception('Wrong header.')
            lines = lines[1:]
        if len(lines) < 2:
            raise Exception('File is empty.')
        lists = []
        for line in lines:
            if line.strip() != '0,1' and line.strip() != '1,0':
                raise Exception('Data is wrong.')
            lists.append([int(num) for num in line.strip().split(',')])
        return lists

    class Calculations:
        def counts(self, lists):
            return [sum(list[0] for list in lists), sum(list[1] for list in lists)]

        def fractions(self, heads, tails):
            sum = heads + tails
            return [heads / sum * 100, tails / sum * 100]


if __name__ == '__main__':
    try:
        research = Research(sys.argv[1])
        result = research.file_reader()
        print(result)
        counts = research.calculator.counts(result)
        print(counts[0], counts[1])
        fractions = research.calculator.fractions(counts[0], counts[1])
        print(fractions[0], fractions[1])
    except Exception as e:
        print(e, file=sys.stderr)