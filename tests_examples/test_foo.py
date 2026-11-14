# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 15:51
# Описание: это пара тестов для браузерного расширения. Первый открывает example.com и проверяет, 
# что на странице появился текст «Changed by my-extension», то есть расширение что-то изменило. 
# Второй формирует адрес chrome-extension:// по фикстуре extension_id, открывает popup.html и 
# проверяет текст внутри всплывающего окна.
from playwright.sync_api import expect, Page


def test_example_test(page: Page) -> None:
    page.goto("https://example.com")
    expect(page.locator("body")).to_contain_text("Changed by my-extension")


def test_popup_page(page: Page, extension_id: str) -> None:
    page.goto(f"chrome-extension://{extension_id}/popup.html")
    expect(page.locator("body")).to_have_text("my-extension popup")