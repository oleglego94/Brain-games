"""Logic of game: even check"""


import random
from brain_games import game_engine


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


def start_game():
    start_msg = 'Answer "yes" if number even, otherwise answer "no".\n'
    the_game = game_engine.flow_the_game(start_msg, generate_qa)
    return the_game
