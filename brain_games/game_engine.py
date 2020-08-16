"""Logic of games"""


import prompt
from brain_games.scripts import brain_games


def play(game):
    brain_games.main()
    print(f'{game.START_MSG}\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    number_of_questions = 3
    i = 0
    while i != number_of_questions:
        question, answer = game.generate_qa()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(answer):
            print("Correct!\n")
            i += 1
        else:
            end_msg = f"""
'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.
Let's try again, {name}!"""
            print(end_msg)
            return
    print(f"Congratulations, {name}!")
