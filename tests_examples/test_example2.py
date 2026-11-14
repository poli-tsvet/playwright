# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 15:30
# Описание: здесь настраивается контекст браузера до запуска теста: устанавливается часовой пояс и язык интерфейса. 
# Затем в тесте проверяются два свойства объекта navigator: строка userAgent и массив languages
import pytest

@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_browser_context_args(page):
    assert page.evaluate("window.navigator.userAgent") == "Europe/Berlin"
    assert page.evaluate("window.navigator.languages") == ["de-DE"]