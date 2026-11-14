# Фио: Цветкова Полина Анатольевна
# Дата: 11.11.2026
# Время: 20:28
# Описание: этот скрипт открываает Chromium, заходит на playwright.dev, 
# делает скриншот в example.png, закрывает браузер
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="example.png")
    browser.close()