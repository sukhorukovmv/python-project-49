import operator
import random

from prompt import string

GAME_RULES = "What is the result of the expression?"
RANGE_NUMBER = (1, 10)


def generate_round() -> tuple[bool, str, str]:
    """Execute one game round and return if answer was correct."""
    # Словарь операций и их символов
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    op_symbol = random.choice(list(operations.keys()))
    op_func = operations[op_symbol]

    a = random.randint(*RANGE_NUMBER)
    b = random.randint(*RANGE_NUMBER)

    question = f"{a} {op_symbol} {b}"
    print(f"Question: {question}")
    user_answer = string("Your answer: ")
    correct_answer = str(op_func(a, b))

    return user_answer.lower() == correct_answer, user_answer, correct_answer
