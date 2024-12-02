import time

from faker import Faker

fake = Faker()

def test_fill_form(home_page, forms_page):
    home_page.visit()
    home_page.click_on_forms_card()
    forms_page.click_on_practice_forms_button()
    forms_page.student_registration_form_should_be_visible()
    forms_page.fill_first_name(fake.first_name())
    forms_page.fill_last_name(fake.last_name())
    forms_page.fill_email(fake.email())
    forms_page.choose_gender(fake.passport_gender())
    forms_page.fill_mobile_number(str(fake.random_number(10)))
    forms_page.choose_hobby(fake.random_element(elements=("sports", "reading", "music")))
    time.sleep(3)
    forms_page.click_submit_button()
    time.sleep(3)
    forms_page.thanks_popup_should_be_visible()

