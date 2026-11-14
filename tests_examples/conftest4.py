# Фио: Цветкова Полина Анатольевна
# Дата: 10.11.2026
# Время: 21:35
# Описание: Две фикстуры для тестов с браузерным расширением. 
# Первая запускает постоянный профиль Chromium и подключает расширение из локальной папки. 
# Вторая достаёт ID этого расширения из адреса chrome-extension://<id>/
from typing import Generator
from pathlib import Path
from playwright.sync_api import Playwright, BrowserContext
import pytest


@pytest.fixture()
def context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    path_to_extension = Path(__file__).parent.joinpath("my-extension")
    context = playwright.chromium.launch_persistent_context(
        "",
        channel="chromium",
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    yield context
    context.close()


@pytest.fixture()
def extension_id(context) -> Generator[str, None, None]:
    # for manifest v3:
    service_worker = context.service_workers[0]
    if not service_worker:
        service_worker = context.wait_for_event("serviceworker")

    extension_id = service_worker.url.split("/")[2]
    yield extension_id
