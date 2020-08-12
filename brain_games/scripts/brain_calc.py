#!/usr/bin/env python3
"""Run script for game: calculator"""


from brain_games.games import game_engine, calc_logic


def main():
    start_msg = 'What is the result of the expression?\n'
    game_engine.play_game(start_msg, calc_logic.generate_qa)


if __name__ == '__main__':
    main()
