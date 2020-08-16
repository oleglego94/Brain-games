#!/usr/bin/env python3
"""Run script for game: prime check"""


from brain_games.games import prime
from brain_games import game_engine


def main():
    game_engine.play(prime)


if __name__ == '__main__':
    main()
