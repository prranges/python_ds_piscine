import sys
from random import randint

class Research:
    def __init__(self, file):
        self.file = file
        self.calculator = self.Calculations(self.file_reader())
        self.analytics = self.Analytics(self.file_reader())


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
        def __init__(self, lists):
            self.lists = lists    
        
        def counts(self):
            return [sum(list[0] for list in self.lists), sum(list[1] for list in self.lists)]

        def fractions(self, heads, tails):
            sum = heads + tails
            return [heads / sum * 100, tails / sum * 100]

    class Analytics(Calculations):
        def __init__(self, lists):
            super().__init__(lists)

        def predict_random(self, n):
            result = []
            for i in range(n):
                head = randint(0, 1)
                tail = 1 if head == 0 else 0
                result.append([head, tail])
            return result

        def predict_last(self):
            return self.lists[-1]


if __name__ == '__main__':
    try:
        research = Research(sys.argv[1])
        result = research.file_reader()
        print(result)
        counts = research.calculator.counts()
        print(counts[0], counts[1])
        fractions = research.calculator.fractions(counts[0], counts[1])
        print(fractions[0], fractions[1])
        predict_random = research.analytics.predict_random(3)
        print(predict_random)
        predict_last = research.analytics.predict_last()
        print(predict_last)
    except Exception as e:
        print(e, file=sys.stderr)