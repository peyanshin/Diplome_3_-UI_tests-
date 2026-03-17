import allure

from curl import *
from pages.order_page import OrderPage
from data import *


class TestOrdersListPageButtons:
    @allure.description("Проверка попадания заказа «В работу» после его оформления")
    def test_all_time_orders_counter(self, driver):
        order_page = OrderPage(driver)
        with allure.step("Сформировать заказ"):
            order_page.prepare_order()
        with allure.step("Войти в аккаунт"):
            order_page.login(Credentials.email, Credentials.password)
        with allure.step("Оформить заказ"):
            order_page.make_order()
        with allure.step("Найти на ленте заказов наш заказ в разделе «В работе»"):
            order_page.should_have_order_in_work_section()

    @allure.title("Проверка изменения счётчиков заказов")
    @allure.description("Проверка изменения счётчика «Выполнено за всё время»")
    def test_all_day_orders_counter(self, driver):
        order_page = OrderPage(driver)
        with allure.step("Сформировать заказ"):
            order_page.prepare_order()
        with allure.step("Войти в аккаунт"):
            order_page.login(Credentials.email, Credentials.password)
        with allure.step("Оформить заказ"):
            order_page.make_order()
        with allure.step("Убедиться, что счётчик заказов «Выполнено за всё время» изменился (соответствует номеру нашего заказа)"):
            order_page.should_have_correct_all_orders_counter()

    @allure.description("Проверка изменения счётчика «Выполнено за сегодня»")
    def test_today_orders_counter(self, driver):
        order_page = OrderPage(driver)
        with allure.step("Определить текущее значение счётчика заказов «Выполнено за сегодня»"):
            order_page.corrent_today_orders_counter()
        with allure.step("Сформировать заказ"):
            order_page.prepare_order()
        with allure.step("Войти в аккаунт"):
            order_page.login(Credentials.email, Credentials.password)
        with allure.step("Оформить заказ"):
            order_page.make_order()
        with allure.step("Убедиться, что счётчик заказов «Выполнено за сегодня» изменился (стал больше на единицу)"):
            order_page.should_have_correct_today_orders_counter()
