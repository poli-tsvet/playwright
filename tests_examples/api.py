# Фио: Цветкова Полина Анатольевна
# Дата: 12.11.2026
# Время: 10:57
# Описание: Здесь настраивается доступ к GitHub API. 
# Сначала проверяется, что в окружении есть переменная GITHUB_API_TOKEN (иначе тест упадёт ещё до запуска).
# Затем создаётся фикстура на уровне всей сессии: она собирает контекст для HTTP-запросов к api.github.com, 
# добавляет к каждому запросу авторизацию по токену и заголовок для GitHub API версии v3. 
# Этот контекст передаётся в тесты, а после завершения работы корректно закрывается.
import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        # We set this header per GitHub guidelines.
        "Accept": "application/vnd.github.v3+json",
        # Add authorization token to all requests.
        # Assuming personal access token available in the environment.
        "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()
