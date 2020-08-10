"""Logic of game: prime check"""


from brain_games.games import game_engine
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


start_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'  # noqa: E501
game_engine.play_game(start_msg, generate_qa)
