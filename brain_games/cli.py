"""User name request"""


import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name
