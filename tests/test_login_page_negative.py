import pytest

from tests.test_login_page import URL, USERNAME, PASSWORD
from page_objects.login_page import LoginPage



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
        
        ## Go to webpage

        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(user = username, pw = password)

        assert login_page.get_error_message() == expected_error_message