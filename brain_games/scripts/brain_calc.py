"""Start script for game: calculator"""


from brain_games.scripts import brain_games
from brain_games.games import calcgame_logic


def main():
    brain_games.main()
    calcgame_logic.play_game()


if __name__ == '__main__':
    main()
