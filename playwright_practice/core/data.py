import json
from playwright.sync_api import Page, expect
from faker import Faker

base_url = "https://demoqa.com/"

class DataGenerator():
    def __init__(self):
        self.faker = Faker()

    def generate_data(self):
        return {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'email': self.faker.email(),
            'gender': self.faker.passport_gender(),
            'mobile_number': self.faker.random_number(10),
            'hobby': self.faker.random_elements(elements=('sports', 'reading', 'music'))
        }

    @staticmethod
    def wright_data_to_json(data):
        with open('data_for_form.json', 'a', encoding='utf-8') as json_file: json.dump(data, json_file, indent=4)
