import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем станицу {url}")
    def open_page(self, url):
        self.driver.get(url)

    def get_text_of_element(self, element):
        return self.driver.find_element(*element).text

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def fill_the_field(self, field_name, user_input):
        self.driver.find_element(*field_name).send_keys(user_input)

    def wait_for_url_changed(self, url):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_changes(url))

    def get_current_url(self):
        return self.driver.current_url

    def get_current_attribute(self, element, attribute):
        return  self.driver.find_element(*element).get_attribute(attribute)

    def wait_for_element_invisibility(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(element))

    def wait_for_element_clickable(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(element))

    def drag_and_drop_script(self, draggable_elem, droppable_elem):
        draggable = self.driver.find_element(*draggable_elem)
        droppable = self.driver.find_element(*droppable_elem)
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            draggable,
            droppable
        )

