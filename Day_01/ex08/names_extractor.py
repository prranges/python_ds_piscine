import sys

def extract_name(file):
    with open(file, 'r') as input:
        with open('employees.tsv', 'w') as output:
            output.write('Name\tSurname\tE-mail\n')
            for line in input:
                name = line.split('.')[0].strip().capitalize()
                surname = line.split('.')[1].strip().split('@')[0].capitalize()
                output.write(f'{name}\t{surname}\t{line}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        extract_name(sys.argv[1])