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

url_to_test = 'https://automationexercise.com/'

def test9():
    driver.get(url_to_test)
    assert driver.current_url == url_to_test
    assert driver.title == "Automation Exercise"
    overlay_close_button = driver.find_element("xpath", "//button[contains(@class, 'close-overlay')]")
    overlay_close_button.click()
    button_products = "//a[@href='/products']"
    driver.find_element("xpath",button_products).click()
    assert driver.current_url == "https://automationexercise.com/products"
#    time.sleep(120)
#    locator_dialog_overlay = "//div[@class='/fc-dialog-overlay']"
#    driver.find_element("xpath",locator_dialog_overlay).click()
    locator_allproducts = "//h2[@class='/title text-center']"
    assert driver.find_element("xpath",locator_allproducts) == "All Products"
