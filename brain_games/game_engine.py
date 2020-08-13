"""Logic of games"""


import prompt
from brain_games.scripts import brain_games
from brain_games.cli import welcome_user


def flow_the_game(start_msg, generate_qa):
    brain_games.main()
    print(start_msg)
    name = welcome_user()
    number_of_questions = 3
    i = 0
    while i != number_of_questions:
        question, answer = generate_qa()
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
            break
    if i == 3:
        print(f"Congratulations, {name}!")
