import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    YANDEX_LOGO = By.XPATH, './/img[@alt="Yandex"]'
    SCOOTER_LOGO = By.XPATH, './/img[@alt = "Scooter"]'
    ORDER_BUTTON_HEADER = By.XPATH, './/div[contains(@class, "Header")]//button[text()="Заказать"]'

    @allure.step("Клик на логотип Яндекса")
    def click_to_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Клик на кнопку заказа")
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON_HEADER)

    @allure.step("Клик на логотип Самокаты")
    def click_to_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
