from selenium.webdriver.common.by import By


class LocatorsMain:

    # header
    YANDEX_LOGO = By.XPATH, './/img[@alt="Yandex"]'
    SCOOTER_LOGO = By.XPATH, './/img[@alt = "Scooter"]'
    ORDER_BUTTON_HEADER = By.XPATH, './/div[contains(@class, "Header")]//button[text()="Заказать"]'

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
