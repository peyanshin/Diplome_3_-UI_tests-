import allure

from curl import *
from pages.main_page import MainPage

class TestMainPage:
    @allure.title("Проверка работы кнопок главной страницы")
    @allure.description("Проверка работы кнопки Лента заказов")
    def test_push_orders_list_button(self, driver):
        main_page = MainPage(driver)
        with allure.step("Нажать кнопку Лента заказов"):
            main_page.click_orders_list_button()
        with allure.step("Проверить, что открыта Лента заказов"):
            assert main_page.check_current_url_contains(feed_page), "URL не содержит ожидаемый домен ленты заказов"

    @allure.description("Проверка работы кнопки Конструктор")
    def test_push_construction_button(self, driver):
        main_page = MainPage(driver)
        with allure.step("Нажать кнопку Конструктор"):
            main_page.click_construction_button()
        with allure.step("Проверить, что открыт Конструктор"):
            assert main_page.check_current_url_contains(main_site), "URL не соответствует ожидаемому домену конструктора"

    @allure.title("Проверка открытия деталей ингредиентов")
    @allure.description("Проверка открытия деталей булки при нажатии на него")
    def test_push_bread_ingredient_button(self, driver):
        main_page = MainPage(driver)
        with allure.step("Нажать на булку"):
            main_page.click_bread_ingredient_button()
        with allure.step("Проверить, что открылось окно Детали ингредиента"):
            assert main_page.is_ingredient_details_visible(), "Окно Детали ингредиента не открылось"
        with allure.step("Закрыть окно Детали ингредиента"):
            main_page.close_window()
        with allure.step("Убедиться, что окно закрылось"):
            assert main_page.is_ingredient_details_hidden(), "Окно Детали ингредиента не закрылось"

    @allure.title("Проверка изменения счётчика ингредиента при его добавлении в корзину")
    @allure.description("Проверка изменения счётчика ингредиента булки при его добавлении в корзину")
    def test_change_ingredient_quantity(self, driver):
        main_page = MainPage(driver)
        with allure.step("Перетащить булку в корзину"):
            main_page.drag_and_drop_bread()
        with allure.step("Получить текущее значение счётчика ингредиента"):
            counter_text = main_page.get_ingredient_counter_text()
        with allure.step("Проверить, что счётчик равен 2"):
            assert counter_text == "2", f"Счётчик ингредиента равен {counter_text}, а не 2"
