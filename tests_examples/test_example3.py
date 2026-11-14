# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 15:38
# Описание: здесь смешаны два фреймворка — unittest (класс с методом test_foobar) и pytest (фикстура page и autouse-метод setup). 
# Фикстура автоматически выполняется перед каждым тестом и передаёт объект страницы в атрибут self.page, 
# чтобы метод теста мог с ним работать. Сам тест делает переход по URL, простая проверка. 
import pytest
import unittest

from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.locator("#foobar").click()
        assert self.page.evaluate("1 + 1") == 2