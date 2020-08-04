#!/usr/bin/env python3
"""Run script for game: arithmetical progression """


from brain_games.scripts import brain_games
from brain_games.games import progression_logic


def main():
    brain_games.main()
    progression_logic.play_game()


if __name__ == '__main__':
    main()
