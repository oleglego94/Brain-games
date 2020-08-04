#!/usr/bin/env python3
"""Run script for game: even check"""


from brain_games.scripts import brain_games
from brain_games.games import even_logic


def main():
    brain_games.main()
    even_logic.play_game()


if __name__ == '__main__':
    main()
