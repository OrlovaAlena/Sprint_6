import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):

    URL = 'https://qa-scooter.praktikum-services.ru/order'

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def get_metro_station_locator(metro_name):
        return By.XPATH, f".//div[@class = 'select-search__select']//*[text()= '{metro_name}']"

    @allure.title("Выбор станции метро из выпадающего списка")
    def choose_metro_station(self, metro_name):
        self.click_element(self.get_metro_station_locator(metro_name))

    @staticmethod
    def get_rental_time_locator(days):
        return By.XPATH, f'.//div[@class="Dropdown-option"][text()="{days}"]'

    @allure.title("Выбор срока аренды из выпадающего списка")
    def choose_rental_time(self, days):
        self.click_element(self.get_rental_time_locator(days))

    @staticmethod
    def get_scooter_color_locator(color):
        return By.XPATH, f'.//label[contains(@class,  "Checkbox")][text()="{color}"]'

    @allure.title("Выбор цвета самоката")
    def choose_scooter_color(self, color):
        self.click_element(self.get_scooter_color_locator(color))

    @allure.title("Скролл до нужной кнопки")
    def click_order_button(self, locator):
        self.scroll_page(locator)
        self.click_element(locator)
