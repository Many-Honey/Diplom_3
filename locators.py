from selenium.webdriver.common.by import By


class RecoverPasswordLocators:
    recover_password_header = (By.XPATH, './/*[text()="Восстановление пароля"]')
    email_field = (By.CSS_SELECTOR, '.text.input__textfield.text_type_main-default')
    recovery_button = (By.XPATH, './/button[text()="Восстановить"]')
    new_password_field = (By.XPATH, './/div[./label[text()="Пароль"]]')
    eye_icon = (By.CSS_SELECTOR, '.input__icon-action')

class LoginPageLocators:
    email_field = (By.XPATH, './/label[text()="Email"]/../input')
    password_field = (By.XPATH, './/label[text()="Пароль"]/../input')
    login_button = (By.XPATH, './/button[text()="Войти"]')
    recover_password_button = (By.XPATH, './/*[text()="Восстановить пароль"]')
    login_header = (By.XPATH, './/*[text()="Вход"]')

class MainPageLocators:
    user_profile_button = (By.XPATH, './/p[text()="Личный Кабинет"]')
    constructor_button = (By.XPATH, './/p[text()="Конструктор"]')
    order_feed_button = (By.XPATH, './/p[text()="Лента Заказов"]')
    constructor_header = (By.XPATH, './/h1[text()="Соберите бургер"]')
    bun = (By.XPATH, './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[1]/a[1]')
    sauce = (By.XPATH, './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[2]/a[1]')
    filling = (By.XPATH, './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[3]/a[1]')
    ingredient_detail_header = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    detail_close_button = (By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]/*/button')
    bun_counter = (By.XPATH, './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/ul[2]/a[1]/div[1]/p')
    burger_constructor_list = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
    make_order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    order_id_text = (By.XPATH, './/p[text()="идентификатор заказа"]')
    order_close_button = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS')

class ProfilePageLocators:
    profile_info_text = (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")
    order_history_button = (By.XPATH, './/a[text()="История заказов"]')
    exit_button = (By.XPATH, './/button[text()="Выход"]')

class OrderFeedPageLocators:
    order_header = (By.XPATH, './/h1[text()="Лента заказов"]')
    first_in_list_oder = (By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]/li[1]/a')
    order_popup = (By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]')
    all_time_counter = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p')
    today_counter = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p')
    in_progress_order = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')


