import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.elements.order_page_elements import LocatorsOrder


class OrderPage(BasePage):

    URL = 'https://qa-scooter.praktikum-services.ru/order'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дождаться страницы заказа")
    def wait_for_order_page(self):
        self.wait_for_url(self.URL)

    @allure.step("Скролл до кнопки заказа")
    def click_order_button(self, locator):
        self.scroll_page(locator)
        self.click_element(locator)

    @allure.step("Ввод имени")
    def fill_name(self, name):
        self.fill_input(LocatorsOrder.NAME_INPUT, name)

    @allure.step("Ввод фамилии")
    def fill_last_name(self, last_name):
        self.fill_input(LocatorsOrder.LAST_NAME_INPUT, last_name)

    @allure.step("Ввод адреса")
    def fill_address(self, address):
        self.fill_input(LocatorsOrder.ADDRESS_INPUT, address)

    @allure.step("Ввод телефонного номера")
    def fill_telephone_number(self, number):
        self.fill_input(LocatorsOrder.TELEPHONE_NUMBER_INPUT, number)

    @allure.step("Ввод станции метро")
    def fill_metro(self, metro_station):
        self.fill_input(LocatorsOrder.METRO_INPUT, metro_station)

    @allure.step("Ввод дня доставки")
    def fill_delivery_date(self, delivery_date):
        self.fill_input(LocatorsOrder.DATE_INPUT, delivery_date)

    @allure.step("Ввод комментария")
    def fill_comment(self, comment):
        self.fill_input(LocatorsOrder.COMMENT_INPUT, comment)

    @staticmethod
    def find_metro_station(metro):
        return By.XPATH, f"{LocatorsOrder.METRO_PART_1}{metro}{LocatorsOrder.END}"

    @allure.step("Выбор станции метро из выпадающего списка")
    def choose_metro_station(self, metro_station):
        self.click_element(self.find_metro_station(metro_station))

    @allure.step("Клик на кнопку 'далее'")
    def click_next_step_button(self):
        self.click_element(LocatorsOrder.NEXT_STEP_ORDER_BUTTON)
        self.wait_for_visible(LocatorsOrder.DATE_INPUT)

    @allure.step("Клик на поле выбора количества дней аренды")
    def click_rental_time(self):
        self.click_element(LocatorsOrder.RENTAL_TIME_FORM)

    @staticmethod
    def get_rental_option_station(days):
        return By.XPATH, f"{LocatorsOrder.RENTAL_TIME_PART_1}{days}{LocatorsOrder.END}"

    @allure.step("Выбор срока аренды из выпадающего списка")
    def select_rental_time(self, days):
        self.click_element(self.get_rental_option_station(days))

    @staticmethod
    def get_scooter_color(color):
        return By.XPATH, f'{LocatorsOrder.COLOR_PART_1}{color}{LocatorsOrder.END}'

    @allure.step("Выбор цвета самоката")
    def select_scooter_color(self, color):
        self.click_element(self.get_scooter_color(color))

    @allure.step("Завершение заказ")
    def complete_order(self):
        self.click_element(LocatorsOrder.COMPLETE_ORDER_BUTTON)

    @allure.step("Подтверждение завершение заказа")
    def confirm_order(self):
        self.click_element(LocatorsOrder.CONFIRM_ORDER_BUTTON)

    @allure.step("Получение текста модального окна")
    def get_text_confirm_modal(self):
        return self.get_text(LocatorsOrder.SUCCESS_ORDER_MODAL)
