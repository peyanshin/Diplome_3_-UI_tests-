import pytest

from curl import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    browser = request.param
    if browser == "Chrome":
        return request.getfixturevalue("driver_Chrome")
    elif browser == "Firefox":
        return request.getfixturevalue("driver_Firefox")

@pytest.fixture(scope="function")
def driver_Chrome():
    options = ChromeOptions()
    options.add_argument("--window-size=2200,1100")
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_Firefox():
    options = FirefoxOptions()
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("signon.generation.enabled", False)
    options.set_preference("security.insecure_field_warning.contextual.enabled", False)
    options.add_argument("--width=2200")
    options.add_argument("--height=1100")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()
