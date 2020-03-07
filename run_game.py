import sys

from game_engine.game_engine import GameEngine


def main():
    with GameEngine() as game:
        game.run()
    sys.exit()

if __name__ == "__main__":
    main()