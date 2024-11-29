import faker.generator
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
#    forms_page.choose_gender(fake.passport_gender())
#    forms_page.fill_mobile_number(fake.phone_number())
#    forms_page.choose_hobby(fake.random_elements(elements=("sports", "reading", "music")))
    forms_page.click_submit_button()
    forms_page.thanks_popup_should_be_visible()

