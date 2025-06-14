# Установка зависимостей проекта
install:
	uv sync

# Запуск приложения brain-games
run:
	uv run brain-games

# Запуск тестов
test:
	uv run pytest

# Запуск тестов с измерением покрытия кода (coverage)
test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

# Проверка кода линтером (ruff)
lint:
	uv run ruff check

# Комбинированная проверка: запуск тестов и линтера
check: test lint

# Сборка проекта
build:
	uv build

# Установка собранного пакета (whl-файла)
package-install:
	uv tool install dist/*.whl
# for reinstall use --force
# uv tool install --force dist/<имя-пакета>
# uv pip list | grep hexlet-code
# не забываем активировать
# source .venv/bin/activate
# brain-games # запускаем после установки

# Файлы, которые не являются реальными файлами (а являются командами)
.PHONY: install test lint selfcheck check build
