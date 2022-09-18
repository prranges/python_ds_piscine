#!/usr/bin/python3

import sys
import psutil

def read_lines(file):
    with open(file, 'r') as input:
        lines = input.readlines()
    return lines

def main(file):
    try:
        lines = read_lines(file)
        for line in lines:
            pass
        process = psutil.Process()
        mem = process.memory_info().rss / (2 ** 30)
        cpu = process.cpu_times()
        print(f'Peak Memory Usage = {mem:.3f} Gb')
        print(f'User Time + System Time = {cpu.user + cpu.system:.2f}s')
    except:
        raise Exception("Error.")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        raise Exception('Argument error. Usage: ./ordinary.py <path to csv file>')