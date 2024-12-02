from playwright.sync_api import Page, expect
# import allure

class FormsPage:
    def __init__(self, page:Page):
        self.page = page

    # @allure.step("Нажимаем на кнопку Practice Form")
    def click_on_practice_forms_button(self):
        self.page.get_by_text("Practice Form").click()

    # @allure.step("Проверяем появление формы для заполнения")
    def student_registration_form_should_be_visible(self):
        expect(self.page.get_by_text("Student Registration Form")).to_be_visible()

    # @allure.step("Заполняем поле ввода имени")
    def fill_first_name(self, first_name):
        self.page.get_by_placeholder("First Name").fill(first_name)

    # @allure.step("Заполняем поле ввода фамилии")
    def fill_last_name(self, last_name):
        self.page.get_by_placeholder("Last Name").fill(last_name)

    # @allure.step("Заполняем поле электронной почты")
    def fill_email(self, email):
        self.page.get_by_placeholder("name@example.com").fill(email)

    # @allure.step("Выбираем пол")
    def choose_gender(self, gender):
        if gender == "M":
            self.page.locator("label[for='gender-radio-1']").check()
        elif gender == "F":
            self.page.locator("label[for='gender-radio-2']").check()
        else:
            self.page.locator("label[for='gender-radio-3']").check()

    # @allure.step("Заполняем поле номер телефона")
    def fill_mobile_number(self, mobile_number):
        self.page.get_by_placeholder("Mobile Number").fill(mobile_number)

    # @allure.step("Выбираем хобби")
    def choose_hobby(self, hobby):
        if hobby == "sports":
            self.page.locator("label[for='hobbies-checkbox-1']").check()
        elif hobby == "reading":
            self.page.locator("label[for='hobbies-checkbox-2']").check()
        else:
            self.page.locator("label[for='hobbies-checkbox-3']").check()

    # @allure.step("Нажимаем кнопку Submit")
    def click_submit_button(self):
        self.page.get_by_text("Submit").click()

    # @allure.step("Проверяем появление всплывающего окна об успешном заполнении")
    def thanks_popup_should_be_visible(self):
        expect(self.page.get_by_text("Thanks for submitting the form")).to_be_visible()
