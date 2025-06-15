import random

from prompt import string

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_NUMBER = (1, 30)


def is_even(number: int) -> int:
    """Check if number is even."""
    return number % 2 == 0


def generate_round() -> tuple[bool, str, str]:
    """Execute one game round and return if answer was correct."""
    number = random.randint(*RANGE_NUMBER)
    correct_answer = "yes" if is_even(number) else "no"

    print(f"Question: {number}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer
