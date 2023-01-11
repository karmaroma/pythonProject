from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, 0.3)

    def get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'id': By.ID,
                    'name': By.NAME,
                    'class_name': By.CLASS_NAME,
                    'part_link': By.PARTIAL_LINK_TEXT,
                    'link': By.LINK_TEXT,
                    'tag': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(exc.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(exc.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(exc.invisibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(exc.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(exc.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)
