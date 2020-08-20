"""Logic of game: arithmetical progression"""


import random


START_MSG = 'What number is missing in the progression?'
SET_LENGTH = 10


def make_question(start, step, miss):
    question = ''
    i = 1
    while i < miss:
        elem = start + step * i
        question += f'{elem} '
        i += 1
    question += '.. '
    i += 1
    while i <= SET_LENGTH:
        elem = start + step * i
        question += f'{elem} '
        i += 1
    return question


def generate_qa():
    start = random.randint(-100, 100)
    step = random.randint(1, 10)
    miss = random.randint(1, SET_LENGTH)
    question = make_question(start, step, miss)
    answer = start + step * miss
    return (question, answer)
