import random
from math import sqrt
from typing import Tuple

from prompt import string

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_NUMBER = (1, 10)


def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number <= 1:
        return False
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def generate_round() -> Tuple[bool, str, str]:
    """Execute one game round and return comparison results."""
    number = random.randint(*RANGE_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"

    print(f"Question: {number}")
    user_answer = string("Your answer: ").lower()

    return user_answer == correct_answer, user_answer, correct_answer
