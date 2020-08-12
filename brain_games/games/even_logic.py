"""Logic of game: even check"""


import random


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_qa():
    question = random.randint(1, 100)
    answer = is_even(question)
    return (question, answer)
