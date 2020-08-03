"""Logic of game: arithmetical progression"""


import random
import prompt
from brain_games.cli import welcome_user



def make_progression(start, step, miss):
    progression = f''
    i = 1
    while i < miss:
        start += step
        progression += f'{start} '
        i += 1
    correct_answer = start + step
    progression += '.. '
    start += step
    while i < 10:
        start += step
        progression += f'{start} '
        i += 1
    return progression, correct_answer


def play_game():
    start_msg = 'What number is missing in the progression?\n'
    print(start_msg)
    name = welcome_user()
    i = 0
    while i != 3:
        start = random.randint(0, 100)
        step = random.randint(1, 10)
        miss = random.randint(1, 10)
        question, correct_answer = make_progression(start, step, miss)
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!\n")
            i += 1
        else:
            end_msg = f"""
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
            print(end_msg)
            break
    if i == 3:
        print(f"Congratulations, {name}!")
