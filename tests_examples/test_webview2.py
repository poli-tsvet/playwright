# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 22:59
# Описание: Этот код открывает сайт playwright.dev, затем по тексту ищет кнопку «Get Started», 
# и через expect проверяет, что она видна. 
from playwright.sync_api import Page, expect


def test_webview2(page: Page):
    page.goto("https://playwright.dev")
    get_started = page.get_by_text("Get Started")
    expect(get_started).to_be_visible()