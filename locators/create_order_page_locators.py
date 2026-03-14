from selenium.webdriver.common.by import By

class CreateOrderPageLocators:
    #Окно создания заказа
    ORD_NUMBER_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]") #номер заказа
    ORD_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]") #кнопка закрытия окна создания заказа
    