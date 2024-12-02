from playwright.sync_api import Page, expect
from playwright_practice.core.data import base_url
# import allure

class HomePage:
    def __init__(self, page:Page):
        self.page = page

    # @allure.step("Открываем home page")
    def visit(self):
        self.page.goto(base_url)

    # @allure.step("Нажимаем на карточку Forms")
    def click_on_forms_card(self):
        self.page.get_by_text("Forms").click()


