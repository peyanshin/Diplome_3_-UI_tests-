from selenium.webdriver.common.by import By

class IngredientPageLocators:
    #Окно деталей ингредиента
    ING_DET_TEXT = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__') and contains(@class, 'text_type_main-large')]") #надпись Детали ингредиента
    ING_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]") #кнопка закрытия окна Детали ингредиента
    MODAL_CONTAINER = (By.CSS_SELECTOR, "div.Modal_modal__container__Wo2l_") #окно деталей ингредиента
    