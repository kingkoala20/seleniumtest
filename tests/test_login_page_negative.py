from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By
import time
import pytest

from test_login_page import URL, USERNAME, PASSWORD

class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        """
        Open page
        Type username incorrectUser into Username field
        Type password Password123 into Password field
        Puch Submit button
        Verify error message is displayed
        Verify error message text is Your username is invalid!
        """
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        ## Go to webpage

        driver.get(URL)


        ## Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        ## Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(PASSWORD)

        ## Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
        time.sleep(2)

        ## Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message not properly displayed"


        ## Verify error message text is Your username is invalid!
        assert error_message_locator.text == "Your username is invalid!", "Error should display 'Your username is invalid!'."
        
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self):
        """
        Open page
        Type username student into Username field
        Type password incorrectPassword into Password field
        Puch Submit button
        Verify error message is displayed
        Verify error message text is Your password is invalid!
        """
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        ## Go to webpage

        driver.get(URL)


        ## Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(USERNAME)

        ## Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")

        ## Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
        time.sleep(2)

        ## Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message not properly displayed"


        ## Verify error message text is Your username is invalid!
        assert error_message_locator.text == "Your password is invalid!", "Error should display 'Your password is invalid!'."
            
        