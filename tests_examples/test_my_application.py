# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 14:59
# Описание:  здесь применяется плагин pytest-playwright. 
# skip_browser("firefox") говорит, что эти тесты не нужно запускать в Firefox.
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import CreateContextCallback
import pytest

@pytest.mark.skip_browser("firefox")

def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")

def test_visit_example(page):
    page.goto("/admin")
    # -> Will result in http://localhost:8080/admin