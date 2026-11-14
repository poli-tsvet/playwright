# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 14:59
# Описание: это тест, который ищет на странице элемент с текстом «Name» и проверяет через expect, 
# что этот элемент виден. На проверку даётся 10 секунд, если элемент не появится за это время, то тест упадёт.
from playwright.sync_api import expect

def test_foobar(page: Page) -> None:
    expect(page.get_by_text("Name")).to_be_visible(timeout=10_000) 