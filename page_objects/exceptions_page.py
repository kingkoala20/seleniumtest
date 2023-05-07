from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ExceptionsPage(BasePage):
    
    _url = "https://practicetestautomation.com/practice-test-exceptions/"
    _row1_field_locator = (By.XPATH, "//div[@id='row1']/input")
    _row1_edit_btn_locator = (By.XPATH, "//div[@id='row1']/button[@id='edit_btn']")
    _row1_add_btn_locator = (By.XPATH, "//div[@id='row1']/button[@id='add_btn']")
    _row1_save_btn_locator = (By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
    _row2_field_locator = (By.XPATH, "//div[@id='row2']/input")
    _row2_save_btn_locator = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    _row2_edit_btn_locator = (By.XPATH, "//div[@id='row2']/button[@id='edit_btn']")
    _confirmation_text = (By.ID, "confirmation")
    _instructions_text = (By.ID, "instructions")
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        
    def open(self):
        self._open_url(self._url)
        
    def row1_click_add_btn(self, time : int = 10):
        super()._click(self._row1_add_btn_locator)
        super()._wait_until_element_visible(self._row2_field_locator, time)
        
    def is_row2_field_displayed(self) -> bool:
        return super()._is_displayed(self._row2_field_locator)
    
    def add_entry(self, text: str):
        super()._type(self._row2_field_locator, text=text)
        super()._click(self._row2_save_btn_locator)
        super()._wait_until_element_visible(self._confirmation_text)
        
    def get_confirmation_text(self) -> str:
        return super()._get_text(self._confirmation_text, time = 3)
    
    def clear_row1_input(self):
        super()._click(self._row1_edit_btn_locator)
        super()._clear_field(self._row1_field_locator)
        
    def edit_entry(self, text: str):
        super()._type(self._row1_field_locator, text)
        super()._click(self._row1_save_btn_locator)
        
    def is_instructions_displayed(self) -> bool:
        super()._click(self._row1_add_btn_locator)
        return super()._is_displayed(self._instructions_text)