URL = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"


from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage

import pytest


class TestPositiveScenarios:
    
    
        
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(USERNAME, PASSWORD)

        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual Url failure!"
        assert logged_in_page.header == "Logged In Successfully", "Header failure!"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible."