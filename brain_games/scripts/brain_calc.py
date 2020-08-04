#!/usr/bin/env python3
"""Run script for game: calculator"""


from brain_games.scripts import brain_games
from brain_games.games import calc_logic


def main():
    brain_games.main()
    calc_logic.play_game()


if __name__ == '__main__':
    main()
