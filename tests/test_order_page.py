import allure
import pytest
from selenium.webdriver.firefox import webdriver

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from src.Elements.main_page_elements import LocatorsMain
from src.Elements.order_page_elements import LocatorsOrder
from src.data import Data


class TestOrderPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.WebDriver()
        cls.driver.get(BasePage.URL)
        cls.page = OrderPage(cls.driver)
        cls.main_page = MainPage(cls.driver)

    @allure.title("Проверка основного флоу заказа с использованием двух наборов тестовых данных")
    @pytest.mark.parametrize(
        'button, name, last_name, address, metro, phone_number, delivery_date, rental_time, color, comment',
        [
            [
                LocatorsMain.ORDER_BUTTON_HEADER, 'Кот', 'Бегемот', 'Садовая, 302-бис кв.50', 'Маяковская',
                '88005553535', '22.04.1935', 'сутки', Data.COLOR_BLACK,
                'Единственно, что может спасти смертельно раненного кота, — это глоток бензина'
            ],
            [
                LocatorsMain.ORDER_BUTTON_PAGE, 'Иван', 'Васильевич', 'Новокузнецкая улица дом 13', 'Новокузнецкая',
                '+7999666362', '17.09.1973', 'трое суток', Data.COLOR_GRAY, ''
            ],
        ]
    )
    def test_make_order(self, button, name, last_name, address, metro, phone_number, delivery_date, rental_time, color,
                        comment):
        self.page.navigate(BasePage.URL)
        self.page.click_order_button(button)
        self.page.wait_for_url(OrderPage.URL)
        self.page.fill_input(LocatorsOrder.NAME_INPUT, name)
        self.page.fill_input(LocatorsOrder.LAST_NAME_INPUT, last_name)
        self.page.fill_input(LocatorsOrder.ADDRESS_INPUT, address)
        self.page.fill_input(LocatorsOrder.METRO_INPUT, metro)
        self.page.choose_metro_station(metro)
        self.page.fill_input(LocatorsOrder.TELEPHONE_NUMBER_INPUT, phone_number)
        self.page.click_element(LocatorsOrder.NEXT_STEP_ORDER_BUTTON)

        self.page.fill_input(LocatorsOrder.DATE_INPUT, delivery_date)
        self.page.click_element(LocatorsOrder.RENTAL_TIME_FORM)
        self.page.choose_rental_time(rental_time)
        self.page.choose_scooter_color(color)
        self.page.fill_input(LocatorsOrder.COMMENT_INPUT, comment)
        self.page.click_element(LocatorsOrder.COMPLETE_ORDER_BUTTON)
        self.page.click_element(LocatorsOrder.CONFIRM_ORDER_BUTTON)
        assert 'Заказ оформлен' in self.page.get_text(LocatorsOrder.SUCCESS_ORDER_MODAL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
