# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 14:59
# Описание: 
# 
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