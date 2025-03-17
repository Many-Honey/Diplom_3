from selenium import webdriver

class WebdriverFactory:
    """Фабрика для создания WebDriver на основе переданного имени браузера."""

    @staticmethod
    def get_webdriver(browser_name):
        """Метод создает и возвращает WebDriver для указанного браузера."""
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

