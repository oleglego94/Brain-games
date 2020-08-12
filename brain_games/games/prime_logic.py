"""Logic of game: prime check"""


import random


def is_prime(num):
    if num == 1:
        return 'no'
    div = 2
    while num % div != 0:
        div += 1
    if div == num:
        return 'yes'
    else:
        return 'no'


def generate_qa():
    question = random.randint(1, 100)
    answer = is_prime(question)
    return (question, answer)
