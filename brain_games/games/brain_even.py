import random

from prompt import string

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 30


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def generate_round():
    """Execute one game round and return if answer was correct."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(number) else "no"

    print(f"Question: {number}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer
