# ФИО: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 15:38
# Описание: Описание: этот код открывает сайт Monkeytype, проверяет, 
# что текущий URL страницы соответствует "https://monkeytype.com/"

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    page.goto("https://monkeytype.com/")
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    
    expect(page).to_have_url("https://monkeytype.com/")