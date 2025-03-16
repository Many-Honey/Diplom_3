import allure

from locators import LoginPageLocators
from pages.base_page import BasePage



class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Нажимаем на кнопку 'Восстановить пароль'")
    def click_on_recover_password_button(self):
        self.click_on(self.locators.recover_password_button)

    @allure.step("Заполняем поле 'Email")
    def fill_the_email_field(self, email):
        self.click_on(self.locators.email_field)
        self.fill_the_field(self.locators.email_field, email)

    @allure.step("Заполняем поле 'Password")
    def fill_the_password_field(self, password):
        self.click_on(self.locators.password_field)
        self.fill_the_field(self.locators.password_field, password)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_on_login_button(self):
        self.click_on(self.locators.login_button)

    def wait_for_login_header_visible(self):
        self.wait_for_element_visible(self.locators.login_header)