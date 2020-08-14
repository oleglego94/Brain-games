#!/usr/bin/env python3
"""Run script for game: arithmetical progression """


from brain_games.games import progression_logic
from brain_games import game_engine


def main():
    game_engine.flow_the_game(progression_logic)


if __name__ == '__main__':
    main()
