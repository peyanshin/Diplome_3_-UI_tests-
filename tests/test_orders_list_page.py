import allure

from curl import *
from pages.order_page import OrderPage
from data import Credentials


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
            actual_text = order_page.get_order_in_work_text()
            assert order_page.order_number in actual_text, (f"Номер заказа {order_page.order_number} не найден в разделе 'В работе'. "f"Фактическое значение: {actual_text}")

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
            actual_text = order_page.get_all_orders_counter_text()
            assert order_page.order_number == actual_text, (f"Номер заказа {order_page.order_number} не совпадает с извлечённым из элемента номером: {actual_text}.")

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
            actual_text = order_page.get_today_orders_counter_text()
            expected_value = int(order_page.today_orders) + 1
            actual_value = int(actual_text)
            assert actual_value == expected_value, (f"Счётчик заказов за сегодня {actual_value} не соответствует ожидаемому {expected_value}")
