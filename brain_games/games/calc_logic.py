"""Logic of game: calculator"""


import random


def generate_qa():
    int1 = str(random.randint(0, 100))
    int2 = str(random.randint(0, 100))
    operator = random.choice('+-*')
    question = f"{int1} {operator} {int2}"
    answer = eval(question)
    return (question, answer)
