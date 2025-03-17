import allure

from helpers import GenerateUserData
from locators import RecoverPasswordLocators
from pages.base_page import BasePage


class RecoverPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecoverPasswordLocators()

    @allure.step("Заполняем поле 'Email")
    def fill_the_email_field(self):
        self.click_on(self.locators.email_field)
        self.fill_the_field(self.locators.email_field, GenerateUserData.email)

    @allure.step("Нажимаем на кнопку 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on(self.locators.recovery_button)

    @allure.step("Нажимаем на иконку 'глаз' в правой части поля 'Пароль'")
    def click_on_eye_icon(self):
        self.click_on(self.locators.eye_icon)

    @allure.step("Получаем значение атрибута 'class' у поля 'Пароль'")
    def get_class_of_new_password_field(self):
        return  self.get_current_attribute(self.locators.new_password_field, "class")

    @allure.step("Ожидаем появления иконки 'глаз' в правой части поля 'Пароль'")
    def wait_for_eye_icon_visible(self):
        self.wait_for_element_visible(self.locators.eye_icon)

    @allure.step("Ожидаем появления заголовка 'Восстановление пароля'")
    def wait_for_recover_password_header_visible(self):
        self.wait_for_element_visible(self.locators.recover_password_header)

    




