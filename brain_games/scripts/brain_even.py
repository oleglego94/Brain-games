"""Start script for game: even check"""


from brain_games.scripts import brain_games
from brain_games import evengame_logic


def main():
    brain_games.main()
    evengame_logic.play_game()


if __name__ == '__main__':
    main()
