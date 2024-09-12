from selenium.webdriver.firefox import webdriver
import allure

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from src.Elements.main_page_elements import LocatorsMain
from src.data import Data


class TestMainPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.WebDriver()
        cls.driver.get(BasePage.URL)
        cls.page = MainPage(cls.driver)

    @allure.title("Проверка ответа на вопрос о цене и способе оплаты")
    def test_price_question_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_1, LocatorsMain.ANSWER_QUESTION_1)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_1)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_1) == Data.EXPECTED_ANSWER_1

    @allure.title("Проверка ответа на вопрос о доступности к заказу нескольких самокатов")
    def test_several_scooters_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_2, LocatorsMain.ANSWER_QUESTION_2)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_2)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_2) == Data.EXPECTED_ANSWER_2

    @allure.title("Проверка ответа о рассчете времени аренды")
    def test_count_rental_time_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_3, LocatorsMain.ANSWER_QUESTION_3)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_3)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_3) == Data.EXPECTED_ANSWER_3

    @allure.title("Проверка ответа о возможности заказа на текущий день")
    def test_rent_for_today_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_4, LocatorsMain.ANSWER_QUESTION_4)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_4)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_4) == Data.EXPECTED_ANSWER_4

    @allure.title("Проверка ответа о возможности изменить время аренды")
    def test_change_rental_time_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_5, LocatorsMain.ANSWER_QUESTION_5)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_5)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_5) == Data.EXPECTED_ANSWER_5

    @allure.title("Проверка ответа о зарядном устройстве")
    def test_charger_availability_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_6, LocatorsMain.ANSWER_QUESTION_6)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_6)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_6) == Data.EXPECTED_ANSWER_6

    @allure.title("Проверка ответа об отмене заказа")
    def test_cancel_order_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_7, LocatorsMain.ANSWER_QUESTION_7)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_7)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_7) == Data.EXPECTED_ANSWER_7

    @allure.title("Проверка ответа о зоне доступности для заказа")
    def test_available_distance_form(self):
        self.page.scroll_page(LocatorsMain.QA_LIST)
        self.page.qa_list_question_click(LocatorsMain.QUESTION_8, LocatorsMain.ANSWER_QUESTION_8)
        self.page.check_element_is_enabled(LocatorsMain.ANSWER_QUESTION_8)
        assert self.page.check_element_has_text(LocatorsMain.ANSWER_QUESTION_8) == Data.EXPECTED_ANSWER_8

    @allure.title("Проверка перехода на страницу Дзена при клике на логотип Яндекс")
    def test_redirect_from_yandex_logo(self):
        self.page.navigate(BasePage.URL)
        self.page.click_element(LocatorsMain.YANDEX_LOGO)
        self.page.switch(MainPage.DZEN_URL)
        assert self.page.get_current_url() == MainPage.DZEN_URL

    @allure.title("Проверка перехода на главную страницу Самокаты при клике на логотип Самокаты")
    def test_redirect_from_scooter_logo(self):
        self.page.navigate(BasePage.URL)
        self.page.click_element(LocatorsMain.ORDER_BUTTON_HEADER)
        self.page.wait_for_url(OrderPage.URL)
        self.page.click_element(LocatorsMain.SCOOTER_LOGO)
        assert self.page.get_current_url() == MainPage.URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
