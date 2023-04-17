from selenium.webdriver.common.by import By
import time
import pytest

from test_login_page import URL, USERNAME, PASSWORD


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "username, password, expected_error_message",
        [
            ("incorrectUser", PASSWORD, "Your username is invalid!"),
            (USERNAME, "incorrectPassword", "Your password is invalid!")
        ]
        )
    def test_negative_login(self, driver, username, password, expected_error_message):
        """
        Open page
        Type username incorrectUser into Username field
        Type password Password123 into Password field
        Puch Submit button
        Verify error message is displayed
        Verify error message text is Your username is invalid!
        """
        

        ## Go to webpage

        driver.get(URL)


        ## Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        ## Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        ## Push Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
        time.sleep(2)

        ## Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message not properly displayed"


        ## Verify error message text is Your username is invalid!
        assert error_message_locator.text == expected_error_message, "Error should display 'Your username is invalid!'."