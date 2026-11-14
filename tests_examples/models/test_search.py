# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 22:30
# Описание: этот код создаёт страницу через browser.new_page(), затем объект SearchPage, после чего вызывает методы
# - navigate() для перехода на сайт и search() для ввода запроса.
from models.search import SearchPage

# in the test
page = browser.new_page()
search_page = SearchPage(page)
search_page.navigate()
search_page.search("search query")