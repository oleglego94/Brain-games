#!/usr/bin/env python3
"""Run script for game: calculator"""


from brain_games.games import calc
from brain_games import game_engine


def main():
    game_engine.play(calc)


if __name__ == '__main__':
    main()
