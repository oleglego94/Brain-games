#!/usr/bin/env python3
"""Run script for game: even check"""


from brain_games.games import game_engine, even_logic


def main():
    start_msg = 'Answer "yes" if number even, otherwise answer "no".\n'
    game_engine.play_game(start_msg, even_logic.generate_qa)


if __name__ == '__main__':
    main()
