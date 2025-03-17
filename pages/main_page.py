import allure

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажимаем на кнопку 'Личный Кабинет'")
    def click_on_user_profile_button(self):
        self.click_on(self.locators.user_profile_button)

    @allure.step("Нажимаем на кнопку 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on(self.locators.constructor_button)

    @allure.step("Нажимаем на кнопку 'Лента Заказов'")
    def click_on_order_feed_button(self):
        self.click_on(self.locators.order_feed_button)

    @allure.step("Ожидаем появления заголовка 'Соберите бургер'")
    def wait_for_constructor_header_visible(self):
        self.wait_for_element_visible(self.locators.constructor_header)

    @allure.step("Нажимаем на булку 'Флюоресцентная булка' в разделе булок")
    def click_on_bun(self):
        self.click_on(self.locators.bun)

    @allure.step("Ожидаем появления заголовка 'Детали ингредиента'")
    def wait_for_ingredient_detail_header_visible(self):
        self.wait_for_element_visible(self.locators.ingredient_detail_header)

    @allure.step("Подтверждаем видимость заголовка 'Детали ингредиента'")
    def ingredient_detail_header_is_displayed(self):
        return self.driver.find_element(*self.locators.ingredient_detail_header).is_displayed()

    @allure.step("Нажимаем на иконку 'крестик'")
    def click_on_close_button(self):
        self.click_on(self.locators.detail_close_button)

    @allure.step("Ожидаем исчезновения заголовка 'Детали ингредиента'")
    def wait_for_ingredient_detail_header_invisibility(self):
        self.wait_for_element_invisibility(self.locators.ingredient_detail_header)

    @allure.step("Нажимаем и перетаскиваем булку 'Флюоресцентная булка' в конструктор")
    def drag_and_drop_sauce(self):
        self.drag_and_drop_script(self.locators.sauce, self.locators.burger_constructor_list)

    @allure.step("Нажимаем и перетаскиваем соус 'Spicy-X' в конструктор")
    def drag_and_drop_bun(self):
        self.drag_and_drop_script(self.locators.bun, self.locators.burger_constructor_list)

    @allure.step("Получаем значение каунтера соуса 'Spicy-X'")
    def get_count_of_sauce(self):
        return self.get_text_of_element(self.locators.bun_counter)

    @allure.step("Подтверждаем видимость номера заказа")
    def order_id_text_is_displayed(self):
        return self.element_is_displayed(self.locators.order_id_text)

    @allure.step("Ожидаем появления номера заказа")
    def wait_for_order_id_text_is_visible(self):
        self.wait_for_element_visible(self.locators.order_id_text)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_on_make_order_button(self):
        self.click_on(self.locators.make_order_button)

    @allure.step("Ожидаем когда иконка 'крестик' станет кликабельной")
    def wait_for_order_close_button_clickable(self):
        self.wait_for_element_clickable(self.locators.order_close_button)

    @allure.step("Нажимаем на иконку 'крестик'")
    def click_on_order_close_button(self):
        self.click_on(self.locators.order_close_button)

    @allure.step("Ожидаем когда кнопка 'Лента заказов' станет кликабельной")
    def wait_for_order_feed_button_clickable(self):
        self.wait_for_element_clickable(self.locators.order_feed_button)

    @allure.step("Ожидаем когда кнопка 'Оформить заказ' станет кликабельной")
    def wait_for_make_order_button_clickable(self):
        self.wait_for_element_clickable(self.locators.make_order_button)






