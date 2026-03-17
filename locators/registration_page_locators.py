from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    #Окно регистрации
    REG_NAME = (By.XPATH, "//input[@name='name' and contains(@class, 'input__textfield')]") #поле ввода Имя в окне Регистрации
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #поле ввода Email в окне Регистрации
    REG_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #поле ввода Пароля в окне Регистрации
    REG_FIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa") #кнопка Зарегистрироваться
    LOG_REG_BUTTON = (By.XPATH, "//a[@href='/login' and text()='Войти']") #кнопка Войти в окне Регистрации
    WRO_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and contains(text(), 'Некорректный пароль')]") #Появление подсказки Некорректный пароль
