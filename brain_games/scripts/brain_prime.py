#!/usr/bin/env python3
"""Run script for game: prime check"""


from brain_games.games import game_engine, prime_logic


def main():
    start_msg = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'  # noqa: E501
    game_engine.play_game(start_msg, prime_logic.generate_qa)


if __name__ == '__main__':
    main()
