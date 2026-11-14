# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 22:49
# Описание: функция pan имитирует движение пальцем (touchstart, touchmove, touchend), чтобы сдвинуть карту. 
# тест открывает Google Maps на Pixel 7, закрывает всплывающее окно, пять раз двигает карту и делает скриншот. 
# запуск через sync_playwright
from playwright.sync_api import sync_playwright, expect

def pan(locator, deltaX=0, deltaY=0, steps=5):
    bounds = locator.bounding_box()
    centerX = bounds['x'] + bounds['width'] / 2
    centerY = bounds['y'] + bounds['height'] / 2

    touches = [{
        'identifier': 0,
        'clientX': centerX,
        'clientY': centerY,
    }]
    locator.dispatch_event('touchstart', {
        'touches': touches,
        'changedTouches': touches,
        'targetTouches': touches
    })

    for i in range(1, steps + 1):
        touches = [{
            'identifier': 0,
            'clientX': centerX + deltaX * i / steps,
            'clientY': centerY + deltaY * i / steps,
        }]
        locator.dispatch_event('touchmove', {
            'touches': touches,
            'changedTouches': touches,
            'targetTouches': touches
        })

    locator.dispatch_event('touchend')

def test_pan_gesture_to_move_the_map(page):
    page.goto('https://www.google.com/maps/place/@37.4117722,-122.0713234,15z', wait_until='commit')
    page.get_by_role('button', name='Keep using web').click()
    expect(page.get_by_role('button', name='Keep using web')).not_to_be_visible()
    met = page.locator('[data-test-id="met"]')
    for _ in range(5):
        pan(met, 200, 100)
    page.screenshot(path="screenshot.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(**p.devices['Pixel 7'])
    page = context.new_page()
    test_pan_gesture_to_move_the_map(page)
    browser.close()