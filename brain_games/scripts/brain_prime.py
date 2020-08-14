#!/usr/bin/env python3
"""Run script for game: prime check"""


from brain_games.games import prime_logic
from brain_games import game_engine


def main():
    game_engine.flow_the_game(prime_logic)


if __name__ == '__main__':
    main()
