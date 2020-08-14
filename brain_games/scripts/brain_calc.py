#!/usr/bin/env python3
"""Run script for game: calculator"""


from brain_games.games import calc_logic
from brain_games import game_engine


def main():
    game_engine.flow_the_game(calc_logic)


if __name__ == '__main__':
    main()
