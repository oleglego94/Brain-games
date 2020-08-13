"""Logic of game: calculator"""


import random
import operator
from brain_games import game_engine


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


def start_game():
    start_msg = 'What is the result of the expression?\n'
    the_game = game_engine.flow_the_game(start_msg, generate_qa)
    return the_game
