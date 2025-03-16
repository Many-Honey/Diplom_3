import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_profile_page import UserProfilePage
from urls import Urls


class TestUserProfile:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_user_profile_by_click_on_profile_button(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.wait_for_user_profile_button_visible()
        main_page.wait_for_user_profile_button_clickable()
        main_page.click_on_user_profile_button()
        profile_page = UserProfilePage(driver)
        profile_page.wait_for_profile_info_text_visible()

        assert profile_page.get_current_url() == Urls.user_profile_url

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_go_to_order_history_by_click_on_order_history_button(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.wait_for_user_profile_button_visible()
        main_page.click_on_user_profile_button()
        profile_page = UserProfilePage(driver)
        profile_page.wait_for_order_history_button_visible()
        profile_page.click_on_order_history_button()

        assert profile_page.get_current_url() == Urls.order_history_url

    @allure.title('Проверка выхода из аккаунта по клику на «Выход»')
    def test_exit_from_user_profile(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.wait_for_user_profile_button_visible()
        main_page.click_on_user_profile_button()
        profile_page = UserProfilePage(driver)
        profile_page.wait_for_exit_button_visible()
        profile_page.click_on_exit_button()
        login_page = LoginPage(driver)
        login_page.wait_for_login_header_visible()

        assert login_page.get_current_url() == Urls.login_url




