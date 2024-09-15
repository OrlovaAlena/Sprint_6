import allure
import pytest
from selenium.webdriver.firefox import webdriver

from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage
from src.elements.main_page_elements import LocatorsMain
from src.data import Data


class TestOrderPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.WebDriver()
        cls.driver.get(BasePage.URL)
        cls.page = OrderPage(cls.driver)
        cls.main_page = MainPage(cls.driver)
        cls.header = Header(cls.driver)

    @allure.title("Проверка основного флоу заказа с использованием двух наборов тестовых данных")
    @pytest.mark.parametrize(
        'button, name, last_name, address, metro_station, phone_number, delivery_date, rental_time, color, comment',
        [
            [
                Header.ORDER_BUTTON_HEADER, 'Кот', 'Бегемот', 'Садовая, 302-бис кв.50', 'Маяковская',
                '88005553535', '22.04.1935', 'сутки', Data.COLOR_BLACK,
                'Единственно, что может спасти смертельно раненного кота, — это глоток бензина'
            ],
            [
                LocatorsMain.ORDER_BUTTON_PAGE, 'Иван', 'Васильевич', 'Новокузнецкая улица дом 13', 'Новокузнецкая',
                '+7999666362', '17.09.1973', 'трое суток', Data.COLOR_GRAY, ''
            ],
        ]
    )
    def test_make_order(self, button, name, last_name, address, metro_station, phone_number, delivery_date, rental_time,
                        color, comment):
        self.main_page.open_page()
        self.page.click_order_button(button)
        self.page.wait_for_order_page()
        self.page.fill_name(name)
        self.page.fill_last_name(last_name)
        self.page.fill_address(address)
        self.page.fill_metro(metro_station)
        self.page.find_metro_station(metro_station)
        self.page.choose_metro_station(metro_station)
        self.page.fill_telephone_number(phone_number)
        self.page.click_next_step_button()

        self.page.fill_delivery_date(delivery_date)
        self.page.click_rental_time()
        self.page.select_rental_time(rental_time)
        self.page.select_scooter_color(color)
        self.page.fill_comment(comment)
        self.page.complete_order()
        self.page.confirm_order()
        assert 'Заказ оформлен' in self.page.get_text_confirm_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
