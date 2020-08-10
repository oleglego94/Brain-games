"""Logic of game: even check"""


from brain_games.games import game_engine
import random


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_qa():
    question = random.randint(1, 100)
    answer = is_even(question)
    return (question, answer)


start_msg = 'Answer "yes" if number even, otherwise answer "no".\n'
game_engine.play_game(start_msg, generate_qa)
