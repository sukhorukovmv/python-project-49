import os
import sys

from brain_games.cli import welcome_user
from brain_games.engine import run_game


def main():
    game_name = os.path.basename(sys.argv[0])
    match game_name:  # Используем match для выбора игры
        case "brain-games":
            welcome_user()
            sys.exit(0)
        case "brain-even":
            from brain_games.games.brain_even import GAME_RULES, generate_round
        case "brain-calc":
            from brain_games.games.brain_calc import GAME_RULES, generate_round
        case "brain-gcd":
            from brain_games.games.brain_gcd import GAME_RULES, generate_round
        case "brain-prime":
            from brain_games.games.brain_prime import GAME_RULES, generate_round
        case "brain-progression":
            from brain_games.games.brain_progression import (
                GAME_RULES,
                generate_round,
            )
        case _:
            print(f"Unknown game: {game_name}")
            games = "brain_even, brain_calc, brain-gcd, brain_progression, brain_prime"
            print(f"Available games: {games}")
            sys.exit(1)

    user_name = welcome_user()
    print(GAME_RULES)
    game_result = run_game(generate_round, user_name)
    if game_result == 0:
        print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
