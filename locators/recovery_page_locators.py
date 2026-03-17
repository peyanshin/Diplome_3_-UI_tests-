from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    #Окно восстановления пароля
    REC_EMAIL = (By.XPATH, "//input[@name='name' and @class='text input__textfield text_type_main-default']") #поле email в окне Восстановление пароля
    REC_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']") #кнопка Восстановить в окне Восстановление пароля
    LOG_REC_BUTTON = (By.XPATH, "//a[@href='/login' and text()='Войти']") #кнопка Войти в окне Восстановление пароля
