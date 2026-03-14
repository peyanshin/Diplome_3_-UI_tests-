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
            main_page.check_current_url_contains(feed_page)

    @allure.description("Проверка работы кнопки Конструктор")
    def test_push_construction_button(self, driver):
        main_page = MainPage(driver)
        with allure.step("Нажать кнопку Конструктор"):
            main_page.click_construction_button()
        with allure.step("Проверить, что открыт Конструктор"):
            main_page.check_current_url_contains(main_site)

    @allure.title("Проверка открытия деталей ингредиентов")
    @allure.description("Проверка открытия деталей булки при нажатии на него")
    def test_push_bread_ingredient_button(self, driver):
        main_page = MainPage(driver)
        with allure.step("Нажать на булку и проверить, что открылось окно Детали ингредиента"):
            main_page.click_bread_ingredient_button()
        with allure.step("Закрыть окно Детали ингредиента и убедиться, что оно закрылось"):
            main_page.close_window()  

    @allure.title("Проверка изменения счётчика ингредиента при его добавлении вкорзину")
    @allure.description("Проверка изменения счётчика ингредиента булки его добавлении вкорзину")
    def test_change_ingredient_quantity(self, driver):
        main_page = MainPage(driver)
        with allure.step("Перетащили булку в корзину"):
            main_page.drag_and_drop_bread()
        with allure.step("Убедились, что счётчик ингредиента изменился на 2"):
            main_page.should_have_correct_answer("2")  
