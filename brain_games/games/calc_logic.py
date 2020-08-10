"""Logic of game: calculator"""


from brain_games.games import game_engine
import random


def generate_qa():
    int1 = str(random.randint(0, 100))
    int2 = str(random.randint(0, 100))
    operator = random.choice('*+-')
    question = f"{int1} {operator} {int2}"
    answer = eval(question)
    return (question, answer)


start_msg = 'What is the result of the expression?\n'

game_engine.play_game(start_msg, generate_qa)
