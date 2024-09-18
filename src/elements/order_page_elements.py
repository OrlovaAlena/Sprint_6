from selenium.webdriver.common.by import By

from pages.header import Header
from src.data import Data
from src.elements.main_page_elements import LocatorsMain


class LocatorsOrder:
    # personal data
    NAME_INPUT = By.XPATH, './/input[contains(@placeholder, "Имя")]'
    LAST_NAME_INPUT = By.XPATH, './/input[contains(@placeholder, "Фамилия")]'
    ADDRESS_INPUT = By.XPATH, './/input[contains(@placeholder, "Адрес")]'
    METRO_INPUT = By.XPATH, './/input[contains(@placeholder, "Станция метро")]'
    TELEPHONE_NUMBER_INPUT = By.XPATH, './/input[contains(@placeholder, "Телефон")]'

    # order data
    DATE_INPUT = By.XPATH, './/input[contains(@placeholder, "Когда привезти самокат")]'
    COMMENT_INPUT = By.XPATH, './/input[contains(@placeholder, "Комментарий")]'

    RENTAL_TIME_FORM = By.XPATH, './/span[@class = "Dropdown-arrow"]'
    NEXT_STEP_ORDER_BUTTON = By.XPATH, './/button[text()="Далее"]'
    COMPLETE_ORDER_BUTTON = By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]'
    CONFIRM_ORDER_BUTTON = By.XPATH, './/button[text()="Да"]'

    SUCCESS_ORDER_MODAL = By.XPATH, './/div[contains(@class, "Order_Modal")]'

    # elements with options
    METRO_PART_1 = '//*[@class ="select-search__select"]//*[text()="'
    RENTAL_TIME_PART_1 = './/div[@class="Dropdown-option"][text()="'
    COLOR_PART_1 = './/label[contains(@class,  "Checkbox")][text()="'

    END = '"]'

    ORDER_TEST_DATA = [
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
