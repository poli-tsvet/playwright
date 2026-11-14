# Фио: Цветкова Полина Анатольевна
# Дата: 14.11.2026
# Время: 15:38
# Описание: Этот код запускает Chromium с расширением, используется launch_persistent_context 
# с папкой профиля, а через флаги загружается расширение. 
# Код проверяет, появился ли service worker, и закрывает контекст.
from playwright.sync_api import sync_playwright, Playwright

path_to_extension = "./my-extension"
user_data_dir = "/tmp/test-user-data-dir"


def run(playwright: Playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        channel="chromium",
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    if len(context.service_workers) == 0:
        service_worker = context.wait_for_event('serviceworker')
    else:
        service_worker = context.service_workers[0]

    # Test the service worker as you would any other worker.
    context.close()


with sync_playwright() as playwright:
    run(playwright)