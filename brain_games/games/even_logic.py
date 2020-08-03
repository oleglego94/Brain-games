"""Logic of game: even check"""


import random
import prompt
from brain_games.cli import welcome_user


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def play_game():
    start_msg = 'Answer "yes" if number even, otherwise answer "no".\n'
    print(start_msg)
    name = welcome_user()
    i = 0
    while i != 3:
        question = random.randint(1, 100)
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = is_even(question)
        if answer == correct_answer:
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
