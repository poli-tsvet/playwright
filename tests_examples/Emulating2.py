# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 22:58
# Описание: Функция pinch создаёт два сенсорных касания в центре элемента и через touchstart / touchmove / touchend
# имитирует движение пальцев, direction='in' - сведение пальцев, direction='out' - разведение. 
# Тест открывает Google Maps на устройстве Pixel 7, закрывает окно «Keep using web», проверяет, что оно исчезло, 
# затем пять раз приближает карту через pinch и сохраняет скриншот. 
# Запуск через sync_playwright
from playwright.sync_api import sync_playwright, expect

def pinch(locator, arg):
    bounds = locator.bounding_box()
    centerX = bounds['x'] + bounds['width'] / 2
    centerY = bounds['y'] + bounds['height'] / 2

    deltaX = arg.get('deltaX', 50)
    steps = arg.get('steps', 5)
    stepDeltaX = deltaX / (steps + 1)

    touches = [
        {
            'identifier': 0,
            'clientX': centerX - (deltaX if arg.get('direction') == 'in' else stepDeltaX),
            'clientY': centerY,
        },
        {
            'identifier': 1,
            'clientX': centerX + (deltaX if arg.get('direction') == 'in' else stepDeltaX),
            'clientY': centerY,
        },
    ]
    locator.dispatch_event('touchstart', {
        'touches': touches,
        'changedTouches': touches,
        'targetTouches': touches
    })

    for i in range(1, steps + 1):
        offset = deltaX - i * stepDeltaX if arg.get('direction') == 'in' else stepDeltaX * (i + 1)
        touches = [
            {
                'identifier': 0,
                'clientX': centerX - offset,
                'clientY': centerY,
            },
            {
                'identifier': 1,
                'clientX': centerX + offset,
                'clientY': centerY,
            },
        ]
        locator.dispatch_event('touchmove', {
            'touches': touches,
            'changedTouches': touches,
            'targetTouches': touches
        })

    locator.dispatch_event('touchend', {
        'touches': [],
        'changedTouches': [],
        'targetTouches': []
    })

def test_pinch_in_gesture_to_zoom_out_the_map(page):
    page.goto('https://www.google.com/maps/place/@37.4117722,-122.0713234,15z', wait_until='commit')
    page.get_by_role('button', name='Keep using web').click()
    expect(page.get_by_role('button', name='Keep using web')).not_to_be_visible()
    met = page.locator('[data-test-id="met"]')
    for _ in range(5):
        pinch(met, {'deltaX': 40, 'direction': 'in'})
    page.screenshot(path="screenshot.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(**p.devices['Pixel 7'])
    page = context.new_page()
    test_pinch_in_gesture_to_zoom_out_the_map(page)
    browser.close()