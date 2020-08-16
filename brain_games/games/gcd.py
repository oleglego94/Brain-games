"""Logic of game: greatest common divisor"""


import random


START_MSG = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    if num2 == 0:
        return abs(num1)
    return find_gcd(num2, num1 % num2)


def generate_qa():
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    question = f"{num1} {num2}"
    answer = find_gcd(num1, num2)
    return (question, answer)
