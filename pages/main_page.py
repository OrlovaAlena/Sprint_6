import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    DZEN_URL = 'https://dzen.ru/?yredirect=true'

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

    @allure.title("Переключение на открывшуюся вкладку")
    def switch(self, url):
        self.switch_window()
        self.wait_for_url(url)
