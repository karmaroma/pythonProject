import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.5)
        element1 = driver.find_element(By.CSS_SELECTOR, "#id_123")

        wait = WebDriverWait(driver, 10, 0.3)
        element = wait.until(exc.visibility_of_element_located((By.CSS_SELECTOR, '#id_123')))
