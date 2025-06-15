import sys
from typing import Callable, Tuple

GAME_ROUNDS = 3


def run_game(
    generate_round: Callable[[], Tuple[bool, str, str]], user_name: str
) -> None:
    """Run the game main loop."""

    correct_answers = 0

    while correct_answers < GAME_ROUNDS:
        is_correct, user_answer, correct_answer = generate_round()

        if is_correct:
            print("Correct!")
            correct_answers += 1
        else:
            WRONG_ANSW_MSG = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(WRONG_ANSW_MSG.format(user_answer, correct_answer))
            print(f"Let's try again, {user_name}!")
            return 1
            # correct_answers = 0
    return 0
