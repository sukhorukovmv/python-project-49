import random
from prompt import string


GAME_RULES = "What number is missing in the progression?"
PROGRESSION_LENGTH_RANGE = (5, 10)  # Используем кортеж для диапазонов
START_RANGE = (0, 30)
STEP_RANGE = (1, 30)


def generate_progression(start: int, step: int, length: int) -> list[int]:
    """Generate arithmetic progression."""
    return [start + i * step for i in range(length)]


def generate_round() -> tuple[bool, str, str]:
    """Execute one game round and return comparison results."""
    length = random.randint(*PROGRESSION_LENGTH_RANGE)
    start = random.randint(*START_RANGE)
    step = random.randint(*STEP_RANGE)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    
    question = " ".join(
        ".." if i == hidden_index else str(num)
        for i, num in enumerate(progression)
    )
    
    print(f"Question: {question}")
    user_answer = string("Your answer: ")
    
    correct_answer = str(progression[hidden_index])
    
    return user_answer == correct_answer, user_answer, correct_answer
