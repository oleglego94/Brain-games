#!/usr/bin/env python3
"""Run script for game: arithmetical progression """


from brain_games.games import progression
from brain_games import game_engine


def main():
    game_engine.play(progression)


if __name__ == '__main__':
    main()
