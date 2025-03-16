import allure

from pages.main_page import MainPage
from pages.ordef_feed_page import OrderFeedPage
from urls import Urls


class TestOrderFeed:

    @allure.title('По клику на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_pops_up_window_with_details(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_page(Urls.order_feed_url)
        feed_page.wait_for_order_is_clickable()
        feed_page.click_on_order()
        feed_page.wait_for_order_popup_visible()

        assert feed_page.order_popup_is_displayed() == True

    @allure.title('Заказы из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_is_displayed_in_order_feed(self,driver, make_order):
        number = make_order
        feed_page = OrderFeedPage(driver)
        feed_page.open_page(Urls.order_feed_url)
        feed_page.wait_for_order_header_visible()
        user_order = feed_page.get_user_order_locator(number)
        feed_page.scroll_to_user_order(user_order)

        assert feed_page.user_order_is_displayed(user_order) == True

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_after_make_order_all_time_completed_counter_increased(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button()
        feed_page = OrderFeedPage(driver)
        feed_page.wait_for_all_time_counter_visible()
        start_counter_value = feed_page.get_all_time_counter_value()
        main_page.click_on_constructor_button()
        main_page.wait_for_constructor_header_visible()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.wait_for_make_order_button_clickable()
        main_page.click_on_make_order_button()
        main_page.wait_for_order_close_button_clickable()
        main_page.click_on_order_close_button()
        main_page.wait_for_order_feed_button_clickable()
        main_page.click_on_order_feed_button()
        feed_page.wait_for_all_time_counter_visible()
        final_counter_value = feed_page.get_all_time_counter_value()

        assert start_counter_value < final_counter_value

    @allure.title('При создании нового заказа счётчик "Выполнено за день" увеличивается')
    def test_after_make_order_today_completed_counter_increased(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button()
        feed_page = OrderFeedPage(driver)
        feed_page.wait_for_today_counter_visible()
        start_counter_value = feed_page.get_today_counter_value()
        main_page.click_on_constructor_button()
        main_page.wait_for_constructor_header_visible()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.wait_for_make_order_button_clickable()
        main_page.click_on_make_order_button()
        main_page.wait_for_order_close_button_clickable()
        main_page.click_on_order_close_button()
        main_page.wait_for_order_feed_button_clickable()
        main_page.click_on_order_feed_button()
        feed_page.wait_for_today_counter_visible()
        final_counter_value = feed_page.get_today_counter_value()

        assert start_counter_value < final_counter_value

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_appears_in_inprogress_list(self, driver, make_order):
        order_number = f'0{make_order}'
        feed_page = OrderFeedPage(driver)
        feed_page.open_page(Urls.order_feed_url)
        feed_page.wait_for_in_progress_order_visible()

        assert order_number == feed_page.get_number_of_in_progress_order()




