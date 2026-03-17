import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

import re

TIMEOUT = 20

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Дождаться видимости элемента")
    def see_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться исчезновения элемента")
    def hide_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        if isinstance(locator, str):
            locator = (By.XPATH, locator)
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельности элемента")
    def wait_and_send_keys(self, locator, text, timeout=10):
        try:
            element = self.wait_for_element(locator, timeout)
            element.clear()
            element.send_keys(text)
        except StaleElementReferenceException:
            element = self.wait_for_element(locator, timeout)
            element.clear()
            element.send_keys(text)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить, что URL содержит подстроку")
    def assert_url_contains(self, expected_substring):
        current_url = self.get_current_url()
        assert expected_substring in current_url, (f"Ожидалось, что URL содержит '{expected_substring}', но URL: '{current_url}'")

    @allure.step("Перетащить ингредиент в корзину")
    def drag_and_drop_element(self, source_locator, target_locator, timeout=10):
        source = self.wait_for_element(source_locator, timeout)
        target = self.wait_for_element(target_locator, timeout)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Подождать появления шестизначного номера заказа")
    def wait_for_six_digit_value(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        six_digit_text = WebDriverWait(self.driver, timeout).until(
            lambda _: (
                text := element.text.strip(),
                text if re.fullmatch(r"\d{6}", text) else False
            )[1]
        )
        return six_digit_text

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text
