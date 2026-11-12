# Фио: Цветкова Полина Анатольевна
# Дата: 09.11.2026
# Время: 14:59
# Описание: этот код открывает сайт Python, находит ссылку с текстом "Downloads", кликает по ней
# и проверяет, что на новой странице отображается заголовок "python"
# Я скопировала пример из раздела Installation
import re 
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.python.org/")
    
    expect(page).to_have_title(re.compile("Python"))

def test_get_started_link(page: Page):
    page.goto("https://www.python.org/")
    
    page.get_by_role("link", name="Getting started").click()
    #Ожидается, что на странице будет заголовок с названием «Installation».
    expect(page.get_by_role("heading", name="python")).to_be_visible()