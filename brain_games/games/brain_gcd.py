import random
from math import gcd

from prompt import string

GAME_RULES = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    """Execute one game round and return if answer was correct."""
    # Словарь операций и их символов

    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    correct_answer = str(gcd(a, b))

    print(f"Question: {a} {b}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer
