import pytest
from selenium.webdriver.firefox import webdriver
import allure

from pages.header import Header
from pages.main_page import MainPage
from src.elements.main_page_elements import LocatorsMain
from src.data import Data


class TestMainPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.WebDriver()
        cls.page = MainPage(cls.driver)
        cls.header = Header(cls.driver)

    @allure.title("Проверка ответов на вопросы на главной странице ")
    @pytest.mark.parametrize(
        'question, answer, expected_answer',
        LocatorsMain.MAIN_PAGE_TEST_DATA
    )
    def test_price_question_form(self, question, answer, expected_answer):
        self.page.open_page()
        self.page.qa_list_question_click(question, answer)
        self.page.check_element_is_enabled(answer)
        assert self.page.check_element_has_text(answer) == expected_answer

    @allure.title("Проверка перехода на страницу Дзена при клике на логотип Яндекс")
    def test_redirect_from_yandex_logo(self):
        self.page.open_page()
        self.header.click_to_yandex_logo()
        self.page.switch()
        self.page.wait_to_dzen()
        assert self.page.get_current_url() == Data.DZEN_URL

    @allure.title("Проверка перехода на главную страницу Самокаты при клике на логотип Самокаты")
    def test_redirect_from_scooter_logo(self):
        self.page.open_page()
        self.header.click_order_button()
        self.header.click_to_scooter_logo()
        assert self.page.get_current_url() == MainPage.URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
