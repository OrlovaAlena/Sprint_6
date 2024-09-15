import allure
from pages.base_page import BasePage
from src.data import Data
from src.elements.main_page_elements import LocatorsMain


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверить, что элемент доступен на странице")
    def check_element_is_enabled(self, locator_answer):
        return self.find_element(locator_answer)

    @allure.step("Проверить текст элемента")
    def check_element_has_text(self, locator_answer):
        return self.get_text(locator_answer)

    @allure.step("Кликнуть на элемент")
    def qa_list_question_click(self, locator_question, locator_answer):
        self.click_element(locator_question)
        self.wait_for_visible(locator_answer)

    @allure.step("Переключение на открывшуюся вкладку")
    def switch(self):
        self.switch_window()

    @allure.step("Ожидание страницы Дзена")
    def wait_to_dzen(self):
        self.wait_for_url(Data.DZEN_URL)

    @allure.step("Прокрутка страницы до блока ответов и вопросов")
    def scroll_page_to_qa_list(self):
        self.scroll_page(LocatorsMain.QA_LIST)
