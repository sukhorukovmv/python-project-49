import os
import sys
from importlib import import_module

from brain_games.cli import welcome_user
from brain_games.engine import run_game

GAMES = {
    "brain-even": "brain_games.games.brain_even",
    "brain-calc": "brain_games.games.brain_calc",
    "brain-gcd": "brain_games.games.brain_gcd",
    "brain-prime": "brain_games.games.brain_prime",
    "brain-progression": "brain_games.games.brain_progression",
}


def load_game(game_key: str):
    """Динамически загружает модуль игры."""
    try:
        module = import_module(GAMES[game_key])
        return module.GAME_RULES, module.generate_round
    except KeyError:
        available = ", ".join(GAMES.keys())
        print(f"Unknown game: {game_key}\nAvailable games: {available}")
        raise SystemExit(1)


def main():
    game_name = os.path.basename(sys.argv[0])
    user_name = welcome_user()

    if game_name == "brain-games":
        return

    game_rules, generate_round = load_game(game_name)

    print(game_rules)
    game_result = run_game(generate_round, user_name)
    if game_result == 0:
        print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
