"""Logic of game: arithmetical progression"""


import random


START_MSG = 'What number is missing in the progression?'


def make_set(start, step, miss):
    set_of_numbers = f''
    i = 1
    set_length = 10
    while i < miss:
        elem = start + step * i 
        set_of_numbers += f'{elem} '
        i += 1
    set_of_numbers += '.. '
    i += 1
    while i <= set_length:
        elem = start + step * i 
        set_of_numbers += f'{elem} '
        i += 1
    return set_of_numbers

def generate_qa():
    start = random.randint(-100, 100)
    step = random.randint(1, 10)
    miss = random.randint(1, 10)
    question = make_set(start, step, miss)
    answer = start + step * miss
    return (question, answer)
