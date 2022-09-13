class Research:
    def file_reader(self):
        with open('data.csv', 'r') as input:
            return input.read()


if __name__ == '__main__':
    print(Research().file_reader())