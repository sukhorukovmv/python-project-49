import random
from math import gcd

from prompt import string

GAME_RULES = "Find the greatest common divisor of given numbers."
RANGE_NUMBER = (1, 10)


def generate_round() -> tuple[bool, str, str]:
    """Execute one game round and return if answer was correct."""
    # Словарь операций и их символов

    a = random.randint(*RANGE_NUMBER)
    b = random.randint(*RANGE_NUMBER)

    correct_answer = str(gcd(a, b))

    print(f"Question: {a} {b}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer
