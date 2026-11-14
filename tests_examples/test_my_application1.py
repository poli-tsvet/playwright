# Фио: Цветкова Полина Анатольевна
# Дата: 10.11.2026
# Время: 18:40
# Описание: здесь применяется плагин pytest-playwright. skip_browser("firefox") убирает Firefox из запуска. 
# Фикстура new_context позволяет создавать дополнительные контексты прямо внутри 
# теста: основная page остаётся в стандартном контексте, а page2 — в новом, то есть это изолированные среды
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback
import pytest

@pytest.mark.skip_browser("firefox")

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://example.com")
    context = new_context()
    page2 = context.new_page()
    # page and page2 are in different contexts
def test_visit_example(page):
    page.goto("https://example.com")