import logging
from config import *
from random import randint
import requests
import json

class Research:
    def __init__(self):
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(log_file, mode='w')
        self.logger.addHandler(self.handler)
        self.formatter = logging.Formatter(fmt=logging_format)
        self.handler.setFormatter(self.formatter)
        self.__file_reader = 0

        self.calculator = self.Calculations(self.file_reader(), self.logger)
        self.analytics = self.Analytics(self.file_reader(), self.logger)


    def file_reader(self, has_header=True):
        
        if self.__file_reader != 0:
            self.logger.debug('Read ' + file_path)
        self.__file_reader += 1

        with open(file_path, 'r') as input:
            lines = input.readlines()
        if lines[0].strip() == '0,1' or lines[0].strip() == '1,0':
            has_header = False
        if has_header:
            if len(lines[0].split(',')) != 2:
                self.logger.error('Wrong header.')
                raise Exception('Wrong header.')
            lines = lines[1:]
        if len(lines) == 0:
            self.logger.error('File is empty.')
            raise Exception('File is empty.')
        lists = []
        for line in lines:
            if line.strip() != '0,1' and line.strip() != '1,0':
                self.logger.error('Data is wrong.')
                raise Exception('Data is wrong.')
            lists.append([int(num) for num in line.strip().split(',')])
        return lists

    def send_report(self, message, webhook=None):
        slack_data = {'text': message}
        if webhook is not None:
            requests.post(
                webhook,
                data=json.dumps(slack_data),
                headers={'Content-Type': 'application/json'}
            )

    class Calculations:
        def __init__(self, lists, logger):
            self.lists = lists    
            self.logger = logger
        
        def counts(self):
            self.logger.debug('Calculating the counts of heads and tails')
            return [sum(list[0] for list in self.lists), sum(list[1] for list in self.lists)]

        def fractions(self, heads, tails):
            self.logger.debug('Calculating the fractions of heads and tails')
            sum = heads + tails
            return [heads / sum * 100, tails / sum * 100]

    class Analytics(Calculations):
        def __init__(self, lists, logger):
            super().__init__(lists, logger)

        def predict_random(self, n):
            self.logger.debug('Predict the random of heads and tails')
            result = []
            for i in range(n):
                head = randint(0, 1)
                tail = 1 if head == 0 else 0
                result.append([head, tail])
            return result

        def predict_last(self):
            self.logger.debug('Predict the last of heads and tails')
            return self.lists[-1]

        def save_file(self, data, file_name, extension='txt'):
            self.logger.debug('Save data to ' + file_name + '.' + extension)
            with open(file_name + '.' + extension, 'w') as outfile:
                outfile.write(data)