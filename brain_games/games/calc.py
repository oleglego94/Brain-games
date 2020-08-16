"""Logic of game: calculator"""


import random
import operator


START_MSG = 'What is the result of the expression?'


def calculate(num1, num2, sign):
    if sign == '+':
        result = operator.add(num1, num2)
    if sign == '-':
        result = operator.sub(num1, num2)
    if sign == '*':
        result = operator.mul(num1, num2)
    return result


def generate_qa():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    sign = random.choice('+-*')
    question = f"{num1} {sign} {num2}"
    answer = calculate(num1, num2, sign)
    return (question, answer)
