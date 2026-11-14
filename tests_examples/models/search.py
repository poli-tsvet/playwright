# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 22:18
# Описание: класс описывает одну страницу (bing.com), хранит ссылку на объект page и локатор поля поиска, 
# navigate - переход на сайт, searc - заполнение поля и нажатие Enter. 
# это избавляет от дублирования локаторов в тестах.

class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('[aria-label="Enter your search term"]')

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")
