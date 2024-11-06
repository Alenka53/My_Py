from datetime import time

from fontTools.subset.svg import xpath
from selenium import webdriver
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service)

url_to_test = "https://demoqa.com/"

def test_Alena_open_elements():
    locator1 = '//div[@class="card mt-4 top-card"]'
    driver.get(url_to_test)
    element = (driver.find_element("xpath", locator1))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    check_url = "https://demoqa.com/elements"
    assert driver.current_url == check_url
