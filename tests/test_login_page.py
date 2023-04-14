URL = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"


## Open Browser

# selenium 4 and google chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By
import time
import pytest


class TestPositiveScenarios:
    
    
        
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        ## Go to webpage

        driver.get(URL)
        time.sleep(2)


        ## Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(USERNAME)

        ## Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(PASSWORD)

        ## Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
        time.sleep(2)

        ## Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        post_url = driver.current_url
        assert "practicetestautomation.com/logged-in-successfully/" in post_url


        ## Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        expected_text_list = ['Congratulations', 'Logged In Successfully']
        result_text_locator = driver.find_element(By.XPATH, "//h1[@class='post-title']")
        assert any(map(result_text_locator.text.__contains__, expected_text_list))

        ## Verify button Log out is displayed on the new page
        logout_btn_locator = driver.find_element(By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
        assert logout_btn_locator.is_displayed()