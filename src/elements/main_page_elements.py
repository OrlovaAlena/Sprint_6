from selenium.webdriver.common.by import By

from src.data import Data


class LocatorsMain:
    # button
    ORDER_BUTTON_PAGE = By.XPATH, './/div[contains(@class, "Home_Finish")]//button[text()="Заказать"]'
    # main
    QA_LIST = By.XPATH, './/*[@data-accordion-component="Accordion"]'
    # headings
    QUESTION_1 = By.XPATH, './/div[@id = "accordion__heading-0"]/parent::div'
    QUESTION_2 = By.XPATH, './/div[@id = "accordion__heading-1"]/parent::div'
    QUESTION_3 = By.XPATH, './/div[@id = "accordion__heading-2"]/parent::div'
    QUESTION_4 = By.XPATH, './/div[@id = "accordion__heading-3"]/parent::div'
    QUESTION_5 = By.XPATH, './/div[@id = "accordion__heading-4"]/parent::div'
    QUESTION_6 = By.XPATH, './/div[@id = "accordion__heading-5"]/parent::div'
    QUESTION_7 = By.XPATH, './/div[@id = "accordion__heading-6"]/parent::div'
    QUESTION_8 = By.XPATH, './/div[@id = "accordion__heading-7"]/parent::div'
    # answer
    ANSWER_QUESTION_1 = By.XPATH, './/div[@id="accordion__panel-0"]/p'
    ANSWER_QUESTION_2 = By.XPATH, './/div[@id="accordion__panel-1"]/p'
    ANSWER_QUESTION_3 = By.XPATH, './/div[@id="accordion__panel-2"]/p'
    ANSWER_QUESTION_4 = By.XPATH, './/div[@id="accordion__panel-3"]/p'
    ANSWER_QUESTION_5 = By.XPATH, './/div[@id="accordion__panel-4"]/p'
    ANSWER_QUESTION_6 = By.XPATH, './/div[@id="accordion__panel-5"]/p'
    ANSWER_QUESTION_7 = By.XPATH, './/div[@id="accordion__panel-6"]/p'
    ANSWER_QUESTION_8 = By.XPATH, './/div[@id="accordion__panel-7"]/p'

    MAIN_PAGE_TEST_DATA = [
                [QUESTION_1,  ANSWER_QUESTION_1, Data.EXPECTED_ANSWER_1],
                [QUESTION_2,  ANSWER_QUESTION_2, Data.EXPECTED_ANSWER_2],
                [QUESTION_3,  ANSWER_QUESTION_3, Data.EXPECTED_ANSWER_3],
                [QUESTION_4,  ANSWER_QUESTION_4, Data.EXPECTED_ANSWER_4],
                [QUESTION_5,  ANSWER_QUESTION_5, Data.EXPECTED_ANSWER_5],
                [QUESTION_6,  ANSWER_QUESTION_6, Data.EXPECTED_ANSWER_6],
                [QUESTION_7,  ANSWER_QUESTION_7, Data.EXPECTED_ANSWER_7],
                [QUESTION_8,  ANSWER_QUESTION_8, Data.EXPECTED_ANSWER_8],
    ]
