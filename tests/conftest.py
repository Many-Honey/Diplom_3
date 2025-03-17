import random
import pytest
import requests

from helpers import GenerateUserData
from pages.login_page import LoginPage
from urls import Urls
from webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    """
    Добавляет аргумент командной строки '--browser' для выбора браузера.
    По умолчанию используется Chrome.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def driver(request):
    """
    Фикстура для создания WebDriver.
    Получает значение браузера из командной строки и передает его в фабрику WebdriverFactory.
    После завершения теста закрывает браузер.
    """
    browser_name = request.config.getoption("--browser")  # Получаем значение из --browser
    driver = WebdriverFactory.get_webdriver(browser_name)  # Создаем WebDriver
    driver.maximize_window()
    yield driver  # Передаем WebDriver в тест
    driver.quit()  # Закрываем браузер после завершения теста`

@pytest.fixture
def user_registration():
    payload = {"email": GenerateUserData.email,
               "password": GenerateUserData.password,
               "name": GenerateUserData.name}
    response_reg = requests.post(Urls.api_register_url, payload)
    yield payload
    # получаем значение accessToken
    r = response_reg.json()
    access_token = r.get("accessToken")
    headers = {"Authorization": f"Bearer{access_token}"}
    requests.delete(Urls.api_user_url, headers=headers)

@pytest.fixture
def user_login(user_registration, driver):
    login_page = LoginPage(driver)
    login_page.open_page(Urls.login_url)
    login_page.fill_the_email_field(user_registration["email"])
    login_page.fill_the_password_field(user_registration["password"])
    login_page.click_on_login_button()
    return login_page


@pytest.fixture
def order_request_body():
    response = requests.get(Urls.api_ingredients_url)
    def random_i(a):
        number = len(a) - 1
        n = random.randint(0, number)
        return n
    ingredients = []
    for i in range(0,2):
        ingredients.append(response.json()["data"][random_i(response.json()["data"])]["_id"])
    payload = {
        "ingredients": ingredients
    }
    return payload


@pytest.fixture
def login_user_api(user_registration):
    payload_login = {
        "email": user_registration.get("email"),
        "password": user_registration.get("password")
    }
    response_login = requests.post(Urls.api_login_url, data=payload_login)
    r = response_login.json()
    access_token = r.get("accessToken")
    headers = {"Authorization": f"Bearer{access_token}"}
    yield headers
    requests.delete(Urls.api_user_url, headers=headers)

@pytest.fixture
def make_order(login_user_api, driver, order_request_body):
    headers = login_user_api
    payload_order = order_request_body
    response_order = requests.post(Urls.api_order_url, data=payload_order, headers=headers)
    order_number = response_order.json()["order"]["number"]
    return order_number
