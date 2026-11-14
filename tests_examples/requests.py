# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 19:43
# Описание: Этот тест с подменой реального API. через page.route перехватывается запрос к пути /api/v1/fruits, 
# а обработчик через route.fulfill отвечает на него фиктивными данными. 
# После этого страница загружается, и проверяется, что элемент с этим названием действительно отображается. 
# поведение интерфейса проверяется на контролируемых данных.

def test_mock_the_fruit_api(page: Page):
    def handle(route: Route):
        json = [{"name": "Strawberry", "id": 21}]
        # fulfill the route with the mock data
        route.fulfill(json=json)

    # Intercept the route to the fruit API
    page.route("*/**/api/v1/fruits", handle)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the Strawberry fruit is visible
    expect(page.get_by_text("Strawberry")).to_be_visible()