import random

from prompt import string

from brain_games.cli import welcome_user

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 30


def is_even(number):
    """Check if number is even."""
    return number % 2 == 0


def str_to_bool(answer):
    """Convert 'yes'/'no' string to boolean."""
    return answer.lower() == "yes"


def get_correct_answer(number):
    """Return correct answer for the game round."""
    return "yes" if is_even(number) else "no"


def play_round():
    """Execute one game round and return if answer was correct."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = get_correct_answer(number)

    print(f"Question: {number}")
    user_answer = string("Your answer: ")

    return user_answer.lower() == correct_answer, user_answer, correct_answer


def main():
    """Run the game main loop."""
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(GAME_RULES)

    correct_answers = 0

    while correct_answers < GAME_ROUNDS:
        is_correct, user_answer, correct_answer = play_round()

        if is_correct:
            print("Correct!")
            correct_answers += 1
        else:
            WRONG_ANSW_MSG = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(WRONG_ANSW_MSG.format(user_answer, correct_answer))
            correct_answers = 0

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
