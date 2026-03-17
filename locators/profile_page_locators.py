from selenium.webdriver.common.by import By

class ProfilePageLocators:
    #Окно профиля
    EXI_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']") #кнопка Выход в окне Профиля
    NAME_TEXT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input[@name='Name']") #поле имя в Профиле
    EMAIL_TEXT = (By.XPATH, "//label[contains(text(), 'Логин')]/following-sibling::input[@name='name']") #поле Email в Профиле
    PASS_TEXT= (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input[@name='name']") #поле Пароль в Профиле
