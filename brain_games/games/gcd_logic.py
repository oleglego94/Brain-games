"""Logic of game: greatest common divisor"""


import random
import prompt
from brain_games.cli import welcome_user


def find_gcd(num1, num2):
    if num1 == 0:
        gcd = num2
    elif num2 == 0:
        gcd = num1
    elif num1 == 1 or num2 == 1:
        gcd = 1
    else:
        gcd = min(num1, num2)
        while gcd >= 0:
            opt1 = num1 % gcd
            opt2 = num2 % gcd
            if opt1 == 0 and opt2 == 0:
                break
            else:
                gcd -= 1
    return gcd


def play_game():
    start_msg = 'Find the greatest common divisor of given numbers.\n'
    print(start_msg)
    name = welcome_user()
    i = 0
    while i != 3:
        int1 = random.randint(0, 100)
        int2 = random.randint(0, 100)
        question = f"{int1} {int2}"
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = str(find_gcd(int1, int2))
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
