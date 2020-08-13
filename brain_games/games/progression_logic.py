"""Logic of game: arithmetical progression"""


import random
from brain_games import game_engine


def make_progression(start, step, miss):
    progression = ''
    i = 1
    progression_length = 10
    while i < miss:
        start += step
        progression += f'{start} '
        i += 1
    correct_answer = start + step
    progression += '.. '
    start = correct_answer
    while i < progression_length:
        start += step
        progression += f'{start} '
        i += 1
    return progression, correct_answer


def generate_qa():
    start = random.randint(-100, 100)
    step = random.randint(1, 10)
    miss = random.randint(1, 10)
    question, answer = make_progression(start, step, miss)
    return (question, answer)


def start_game():
    start_msg = 'What number is missing in the progression?\n'
    the_game = game_engine.flow_the_game(start_msg, generate_qa)
    return the_game
