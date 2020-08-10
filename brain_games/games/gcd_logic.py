"""Logic of game: greatest common divisor"""


from brain_games.games import game_engine
import random


def find_gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        return num2 or num1
    gcd = min(num1, num2)
    while gcd >= 0:
        opt1 = num1 % gcd
        opt2 = num2 % gcd
        if opt1 == 0 and opt2 == 0:
            break
        else:
            gcd -= 1
    return gcd


def generate_qa():
    int1 = random.randint(0, 100)
    int2 = random.randint(0, 100)
    question = f"{int1} {int2}"
    answer = find_gcd(int1, int2)
    return (question, answer)


start_msg = 'Find the greatest common divisor of given numbers.\n'
game_engine.play_game(start_msg, generate_qa)
