"""Logic of game: prime check"""


import random
from brain_games import game_engine


def is_prime(num):
    if num <= 1:
        return False
    div = 2
    while (num//2) % div != 0:
        div += 1
    if div == (num//2):
        return True


def generate_qa():
    question = random.randint(-100, 100)
    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    answer = is_prime(question)
    return (question, answer)


def start_game():
    start_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'  # noqa: E501
    the_game = game_engine.flow_the_game(start_msg, generate_qa)
    return the_game
