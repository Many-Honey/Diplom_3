import time

import allure
from selenium.webdriver.common.by import By

from locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedPageLocators()

    @staticmethod
    def get_user_order_locator(order_number):
        locator = (By.XPATH, f'.//ul[@class="OrderFeed_list__OLh59"]/li/a/div/p[text()="#0{order_number}"]')
        return locator

    def wait_for_order_header_visible(self):
        self.wait_for_element_visible(self.locators.order_header)

    @allure.step("Нажимаем на заказ в разделе 'Лента заказов'")
    def click_on_order(self):
        self.click_on(self.locators.first_in_list_oder)

    def wait_for_order_is_clickable(self):
        self.wait_for_element_clickable(self.locators.first_in_list_oder)

    def wait_for_order_popup_visible(self):
        self.wait_for_element_visible(self.locators.order_popup)

    def order_popup_is_displayed(self):
        return self.element_is_displayed(self.locators.order_popup)

    @allure.step("Скроллим ленту заказов до сделанного заказа")
    def scroll_to_user_order(self, locator):
        self.scroll_to_element(locator)

    def user_order_is_displayed(self, locator):
        return  self.element_is_displayed(locator)

    @allure.step("Получаем значение счетчика 'Выполнено за все время'")
    def get_all_time_counter_value(self):
        return self.get_text_of_element(self.locators.all_time_counter)

    def wait_for_all_time_counter_visible(self):
        self.wait_for_element_visible(self.locators.all_time_counter)

    @allure.step("Получаем значение счетчика 'Выполнено за сегодня'")
    def get_today_counter_value(self):
        return self.get_text_of_element(self.locators.today_counter)

    def wait_for_today_counter_visible(self):
        self.wait_for_element_visible(self.locators.today_counter)

    def wait_for_in_progress_order_visible(self):
        self.wait_for_element_visible(self.locators.in_progress_order)

    def get_number_of_in_progress_order(self):
        return  self.get_text_of_element(self.locators.in_progress_order)





