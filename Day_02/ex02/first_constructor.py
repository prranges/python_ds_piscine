import sys
import os

class Research:
    def __init__(self, file):
        self.file = file

    def file_reader(self):
        if len(sys.argv) != 2:
            raise Exception('To many arguments.')
        if len(self.file.split('.')) != 2:
            raise Exception('Wrong file name.')
        with open(self.file, 'r') as input:
            lines = input.readlines()
            if len(lines[0].split(',')) != 2:
                raise Exception('Wrong header.')
            if len(lines) < 2:
                raise Exception('File is empty.')
            for line in lines[1:]:
                if line.strip() != '0,1' and line.strip() != '1,0':
                    raise Exception('Data is wrong.')
            return ''.join(lines)


if __name__ == '__main__':
    try:
        print(Research(sys.argv[1]).file_reader())
    except Exception as e:
        print(e, file=sys.stderr)