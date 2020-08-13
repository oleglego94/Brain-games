#!/usr/bin/env python3
"""Run script for game: greatest common divisor"""


from brain_games.games import gcd_logic
from brain_games import game_engine


def main():
    start_msg = 'Find the greatest common divisor of given numbers.\n'
    game_engine.play_game(start_msg, gcd_logic.generate_qa)


if __name__ == '__main__':
    main()
