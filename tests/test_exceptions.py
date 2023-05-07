import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    
    
    @pytest.mark.exceptions
    def test_no_such_element(self, driver):
        
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.row1_click_add_btn()
        assert exception_page.is_row2_field_displayed()
        
        
    @pytest.mark.exceptions
    def test_element_not_interactable(self, driver):
        
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.row1_click_add_btn()
        exception_page.add_entry("Banana")
        assert exception_page.get_confirmation_text() == "Row 2 was saved", "Save confirmation text error!"
        
        
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.clear_row1_input()
        exception_page.edit_entry("Sushi")
        assert exception_page.get_confirmation_text() == "Row 1 was saved", f"Text not changed!. Returned: {exception_page.get_confirmation_text()}"
        
    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        assert not exception_page.is_instructions_displayed()
        
    
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeoout_exception(self, driver):
        
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.row1_click_add_btn(time = 6)
        assert exception_page.is_row2_field_displayed()