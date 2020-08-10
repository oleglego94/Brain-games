"""Logic of game: arithmetical progression"""


from brain_games.games import game_engine
import random


def make_progression(start, step, miss):
    progression = ''
    i = 1
    while i < miss:
        start += step
        progression += f'{start} '
        i += 1
    correct_answer = start + step
    progression += '.. '
    start = correct_answer
    while i < 10:
        start += step
        progression += f'{start} '
        i += 1
    return progression, correct_answer


def generate_qa():
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    miss = random.randint(1, 10)
    question, answer = make_progression(start, step, miss)
    return (question, answer)


start_msg = 'What number is missing in the progression?\n'
game_engine.play_game(start_msg, generate_qa)
