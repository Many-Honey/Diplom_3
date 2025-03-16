import allure

from locators import ProfilePageLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfilePageLocators()

    def wait_for_profile_info_text_visible(self):
        self.wait_for_element_visible(self.locators.profile_info_text)

    def wait_for_order_history_button_visible(self):
        self.wait_for_element_visible(self.locators.order_history_button)

    def wait_for_exit_button_visible(self):
        self.wait_for_element_visible(self.locators.exit_button)

    @allure.step("Нажимаем на кнопку 'История заказов'")
    def click_on_order_history_button(self):
        self.click_on(self.locators.order_history_button)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_on_exit_button(self):
        self.click_on(self.locators.exit_button)

