"""Logic of game: even check"""


import random
import prompt
from brain_games.cli import welcome_user


def play_game():
    start_msg = 'Answer "yes" if number even, otherwise answer "no".\n'
    print(start_msg)
    name = welcome_user()
    i = 0
    while i != 3:
        question = random.randint(1, 100)
        even = question % 2 == 0
        odd = question % 2 != 0
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        opt1 = even and answer == "yes"
        opt2 = odd and answer == "no"
        if opt1 or opt2:
            print("Correct!\n")
            i += 1
        else:
            if even:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            end_msg = f"""
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!"""
            print(end_msg)
            break
    if i == 3:
        print(f"Congratulations, {name}!")
