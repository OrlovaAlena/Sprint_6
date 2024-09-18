from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    URL = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def open_page(self):
        self.driver.get(self.URL)

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait_for_visible(locator)
        self.find_element(locator).click()

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def scroll_page(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_visible(locator)
