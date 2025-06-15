import prompt


def welcome():
    print("Welcome to the Brain Games!")


def welcome_user() -> str:
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")  # Добавляем имя в приветствие
    return name
