import pytest
from selenium.webdriver.firefox import webdriver

from pages.base_page import BasePage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.WebDriver()
    driver.get(BasePage.URL)
    driver.quit()

