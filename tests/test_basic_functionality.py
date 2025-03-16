import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.ordef_feed_page import OrderFeedPage
from tests.conftest import driver
from urls import Urls


class TestBasicFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_through_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.login_url)
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        main_page.wait_for_constructor_header_visible()

        assert main_page.get_current_url() == Urls.base_url

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_through_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.base_url)
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_order_header_visible()

        assert order_feed_page.get_current_url() == Urls.order_feed_url

    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_click_on_ingredient_pops_up_window_with_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.base_url)
        main_page.click_on_bun()

        assert main_page.ingredient_detail_header_is_displayed() == True

    @allure.title('Всплывающее окно с деталями закрывается кликом по крестику')
    def test_click_on_close_button_close_window_with_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.base_url)
        main_page.click_on_bun()
        main_page.wait_for_ingredient_detail_header_visible()
        main_page.click_on_close_button()
        main_page.wait_for_user_profile_button_invisibility()

        assert main_page.ingredient_detail_header_is_displayed() == False

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_click_on_ingredient_increases_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.base_url)
        main_page.drag_and_drop_sauce()
        main_page.drag_and_drop_sauce()

        assert main_page.get_count_of_sauce() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_login_user_can_make_order(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.wait_for_constructor_header_visible()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.click_on_make_order_button()

        assert main_page.order_id_text_is_displayed() == True






