# Фио: Цветкова Полина Анатольевна
# Дата: 10.11.2026
# Время: 20:28
# Описание: здесь настраивается эмуляция мобильного устройства. 
# Фикстура не заменяет стандартные аргументы полностью, а дополняет их: 
# берёт «iPhone 11 Pro» (параметры) и сливает с тем, что уже было в browser_context_args
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    iphone_11 = playwright.devices['iPhone 11 Pro']
    return {
        **browser_context_args,
        **iphone_11,
    }