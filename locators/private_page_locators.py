from selenium.webdriver.common.by import By

class PrivatePageLocators:
    #Окно Личный кабинет
    LOG_EMAIL = (By.CSS_SELECTOR, "div.input.input_type_text.input_size_default > input[type='text'][name='name']") #поле ввода Email в окне Личный кабинет
    LOG_PASSWORD = (By.CSS_SELECTOR, "div.input.input_type_password.input_size_default > input[type='password'][name='Пароль']") #поле ввода Пароля в окне Личный кабинет
    LOG_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка Войти в окне Личный кабинет
    REG_BUTTON = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/register"]') #кнопка Зарегистрироваться
    FOG_PAS_BUTTON = (By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']") #кнопка Восстановить пароль
