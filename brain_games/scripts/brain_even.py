#!/usr/bin/env python3
"""Run script for game: even check"""


from brain_games.games import even
from brain_games import game_engine


def main():
    game_engine.play(even)


if __name__ == '__main__':
    main()
