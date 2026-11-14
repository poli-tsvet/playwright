# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 14:59
# Описание: 
# 
import pytest
from playwright.async_api import Page

@pytest.mark.asyncio(loop_scope="session")
async def test_foo(page: Page):
    await page.goto("https://github.com")
    # ...