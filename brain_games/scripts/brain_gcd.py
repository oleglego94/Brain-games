"""Run script for game: greatest common divisor"""


from brain_games.scripts import brain_games
from brain_games.games import gcd_logic


def main():
    brain_games.main()
    gcd_logic.play_game()


if __name__ == '__main__':
    main()
