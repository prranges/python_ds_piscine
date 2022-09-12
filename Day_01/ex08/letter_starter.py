import sys

def start_email(email):
    with open('employees.tsv', 'r') as input:
        file = input.readlines()
        for line in file[1:]:
            name = line.split('\t')[0].strip()
            mail = line.split('\t')[2].strip()
            if mail == email:
                print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        start_email(sys.argv[1])