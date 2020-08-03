"""Run script for game: prime check"""


from brain_games.scripts import brain_games
from brain_games.games import prime_logic


def main():
    brain_games.main()
    prime_logic.play_game()


if __name__ == '__main__':
    main()
