import prompt


def welcome_user() -> str:
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}!")  # Добавляем имя в приветствие
    return name
