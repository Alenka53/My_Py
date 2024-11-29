import pytest
from playwright_practice.components.home_page import HomePage
from playwright_practice.components.forms_page import FormsPage
from playwright.sync_api import Page
import allure

@pytest.fixture
def home_page(page:Page):
    return HomePage(page)

@pytest.fixture
def forms_page(page:Page):
    return FormsPage(page)

@pytest.fixture(scope="function", autouse=True)
def video_and_screenshot(page: Page):
    yield  # здесь выполняется тест

    # Сохранить скриншот
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    # Сохранить видео
    video = page.video.path()
    page.context.close()  # Закрыть контекст, чтобы видео сохранилось на диск
    allure.attach.file(
        video,
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )