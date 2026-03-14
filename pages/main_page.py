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
    def check_current_url_contains(self, expected_domain):
        self.assert_url_contains(expected_domain)

    @allure.step("Нажать на булку")
    def click_bread_ingredient_button(self):
        self.click_on_element(MainPageLocators.BRE_DAD_ITEM)
        self.find_element(IngredientPageLocators.ING_DET_TEXT)
        self.see_element(IngredientPageLocators.ING_DET_TEXT)

    @allure.step("Закрыть окно и убедиться, что оно закрылось")
    def close_window(self):
        self.click_on_element(IngredientPageLocators.ING_CLOSE_BUTTON)
        self.hide_element(IngredientPageLocators.MODAL_CONTAINER)

    @allure.step("Перенос булки в корзину")
    def drag_and_drop_bread(self):
        self.drag_and_drop_element(MainPageLocators.BRE_DAD_ITEM,MainPageLocators.BASKET_AREA)

    @allure.step("Проверить, что значение соответствует ожидаемому")
    def should_have_correct_answer(self, expected_text: str):
        element = self.find_element(MainPageLocators.BRE_COUNTER)
        actual_text = element.text
        assert actual_text == expected_text, (f"Значение {expected_text} не соответствует ожидаемому {actual_text}.")
   