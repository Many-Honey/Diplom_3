import allure

from pages.login_page import LoginPage
from urls import Urls
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recover_password_page_from_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.login_url)
        login_page.click_on_recover_password_button()
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.wait_for_recover_password_header_visible()

        assert recover_password_page.get_current_url() == Urls.forgot_password_url

    @allure.title('Ввод почты и клик по кнопке «Восстановить» ведет на страницу сброса пароля')
    def test_go_to_save_new_password_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(Urls.forgot_password_url)
        recover_password_page.fill_the_email_field()
        recover_password_page.click_on_recovery_button()
        recover_password_page.wait_for_url_changed(Urls.forgot_password_url)

        assert recover_password_page.get_current_url() == Urls.reset_password_url

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_on_password_field_eye_icon_makes_field_active(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(Urls.forgot_password_url)
        recover_password_page.fill_the_email_field()
        recover_password_page.click_on_recovery_button()
        recover_password_page.wait_for_eye_icon_visible()
        recover_password_page.click_on_eye_icon()

        assert 'input_status_active' in recover_password_page.get_class_of_new_password_field()
