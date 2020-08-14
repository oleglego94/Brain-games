"""Logic of game: prime check"""


import random


START_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(num):
    if num <= 1:
        return False
    div = 2
    while num % div != 0:
        div += 1
    if div == num:
        return True


def generate_qa():
    question = random.randint(-100, 100)
    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
