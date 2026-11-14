# Фио: Цветкова Полина Анатольевна
# Дата: 10.11.2026
# Время: 20:11
# Описание: здесь ограничивается выбор браузера, тест запустится только в Chromium
import pytest

@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...