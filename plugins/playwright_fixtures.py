import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args) -> dict:
    """Настройка аргументов для запуска браузера"""

    return {
        **browser_type_launch_args,
        "headless": True,
        "args": [
            "--start-maximized",
        ],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args) -> dict:
    """Настройка параметров браузера"""
    browser_context_args.update(no_viewport=True)
    return browser_context_args
