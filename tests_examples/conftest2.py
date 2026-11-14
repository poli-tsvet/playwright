# Фио: Цветкова Полина Анатольевна
# Дата: 10.11.2026
# Время: 20:37
# Описание: здесь задаётся размер окна браузера
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }