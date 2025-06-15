import operator
import random

from prompt import string

GAME_RULES = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 30


def generate_round():
    """Execute one game round and return if answer was correct."""
    # Словарь операций и их символов
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    op_symbol = random.choice(list(operations.keys()))
    op_func = operations[op_symbol]

    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{a} {op_symbol} {b}"
    correct_answer = str(op_func(a, b))

    print(f"Question: {question}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer
