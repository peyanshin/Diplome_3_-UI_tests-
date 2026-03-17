import allure

from pages.base_page import BasePage
from locators.main_page_locators import *
from locators.ingredient_page_locators import *

class MainPage(BasePage):
    @allure.step("Нажать кнопку Лента заказов")
    def click_orders_list_button(self):
        self.click_on_element(MainPageLocators.ORD_LIST_BUTTON)

    @allure.step("Нажать кнопку «Конструктор»")
    def click_construction_button(self):
        self.click_on_element(MainPageLocators.CON_BUTTON)

    @allure.step("Проверить, что текущий URL содержит ожидаемый домен")
    def check_current_url_contains(self, expected_domain: str) -> bool:
        current_url = self.driver.current_url
        return expected_domain in current_url

    @allure.step("Нажать на булку")
    def click_bread_ingredient_button(self):
        self.click_on_element(MainPageLocators.BRE_DAD_ITEM)

    @allure.step("Проверить видимость окна Детали ингредиента")
    def is_ingredient_details_visible(self):
        self.see_element(IngredientPageLocators.ING_DET_TEXT)
        return True

    @allure.step("Проверить скрытие окна Детали ингредиента")
    def is_ingredient_details_hidden(self):
        self.hide_element(IngredientPageLocators.MODAL_CONTAINER)
        return True

    @allure.step("Закрыть окно Детали ингредиента")
    def close_window(self):
        self.click_on_element(IngredientPageLocators.ING_CLOSE_BUTTON)

    @allure.step("Перенос булки в корзину")
    def drag_and_drop_bread(self):
        self.drag_and_drop_element(MainPageLocators.BRE_DAD_ITEM, MainPageLocators.BASKET_AREA)

    @allure.step("Получить текст счётчика ингредиента")
    def get_ingredient_counter_text(self) -> str:
        self.wait_for_element_visibility(MainPageLocators.BRE_COUNTER)
        element = self.find_element(MainPageLocators.BRE_COUNTER)
        return element.text
