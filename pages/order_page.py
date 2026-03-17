import allure

from helper import generate_registration_data
from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators
from locators.private_page_locators import PrivatePageLocators
from locators.orders_list_page_locators import OrdersListPageLocators
from locators.create_order_page_locators import CreateOrderPageLocators
from locators.registration_page_locators import RegistrationPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.order_number = None
        self.today_orders = None

    @allure.step("Зарегистрироваться и войти в аккаунт")
    def sign_and_login(self):
        name, email, password = generate_registration_data()

        self.click_on_element(MainPageLocators.SIG_ACC_BUTTON)
        self.click_on_element(PrivatePageLocators.REG_BUTTON)

        self.wait_and_send_keys(RegistrationPageLocators.REG_NAME, name)
        self.wait_and_send_keys(RegistrationPageLocators.REG_EMAIL, email)
        self.wait_and_send_keys(RegistrationPageLocators.REG_PASSWORD, password)
        self.click_on_element(RegistrationPageLocators.REG_FIN_BUTTON)

        login_email = self.wait_for_element(PrivatePageLocators.LOG_EMAIL)
        login_password = self.wait_for_element(PrivatePageLocators.LOG_PASSWORD)

        login_email.send_keys(email)
        login_password.send_keys(password)
        self.click_on_element(MainPageLocators.ORD_LIST_BUTTON)

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        self.click_on_element(MainPageLocators.PER_ACC_BUTTON)
        self.wait_and_send_keys(PrivatePageLocators.LOG_EMAIL, email)
        self.wait_and_send_keys(PrivatePageLocators.LOG_PASSWORD, password)
        self.click_on_element(PrivatePageLocators.LOG_BUTTON)

    @allure.step("Подготовить заказ к оформлению")
    def prepare_order(self):
        self.drag_and_drop_element(MainPageLocators.BRE_DAD_ITEM, MainPageLocators.BASKET_AREA)

    @allure.step("Оформить заказ")
    def make_order(self):
        self.click_on_element(MainPageLocators.MAKE_ORD_BUTTON)
        self.order_number = self.wait_for_six_digit_value(CreateOrderPageLocators.ORD_NUMBER_TEXT)
        self.click_on_element(CreateOrderPageLocators.ORD_CLOSE_BUTTON)
        self.click_on_element(MainPageLocators.ORD_LIST_BUTTON)
        return self.order_number

    @allure.step("Текущее значение счётчика заказов «Выполнено за сегодня»")
    def corrent_today_orders_counter(self):
        self.click_on_element(MainPageLocators.ORD_LIST_BUTTON)
        element = self.wait_for_element(OrdersListPageLocators.ORD_DAY_NUM_TEXT)
        self.today_orders = element.text.strip()
        self.click_on_element(MainPageLocators.CON_BUTTON)
        return self.today_orders

    @allure.step("Получить текст элемента с номером заказа в разделе 'В работе'")
    def get_order_in_work_text(self):
        element = self.wait_for_element(OrdersListPageLocators.ORD_NUM_WORK_TEXT)
        return element.text

    @allure.step("Получить текущий номер заказа из счётчика «Выполнено за всё время»")
    def get_all_orders_counter_text(self):
        element = self.wait_for_element(OrdersListPageLocators.ORD_NUM_TEXT)
        return element.text.strip()

    @allure.step("Получить текущее значение счётчика заказов за сегодня")
    def get_today_orders_counter_text(self):
        element = self.wait_for_element(OrdersListPageLocators.ORD_DAY_NUM_TEXT)
        return element.text.strip()
