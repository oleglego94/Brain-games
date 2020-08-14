#!/usr/bin/env python3
"""Run script for game: greatest common divisor"""


from brain_games.games import gcd_logic
from brain_games import game_engine


def main():
    game_engine.flow_the_game(gcd_logic)


if __name__ == '__main__':
    main()
