"""Logic of game: calculator"""


import random
import prompt
from brain_games.cli import welcome_user


def play_game():
    start_msg = 'What is the result of the expression?\n'
    print(start_msg)
    name = welcome_user()
    i = 0
    while i != 3:
        int1 = str(random.randint(0, 100))
        int2 = str(random.randint(0, 100))
        operator = random.choice('*+-')
        question = f"{int1} {operator} {int2}"
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = str(eval(question))
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
