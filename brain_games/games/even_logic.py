"""Logic of game: even check"""


import random


START_MSG = 'Answer "yes" if number even, otherwise answer "no".\n'


def is_even(num):
    if num % 2 == 0:
        return True


def generate_qa():
    question = random.randint(-100, 100)
    if is_even(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
