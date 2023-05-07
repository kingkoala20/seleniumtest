from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage

class LoggedInSuccessfullyPage(BasePage):
    
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, "//h1[@class='post-title']")
    __log_out_button_locator = (By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
    
    @property
    def expected_url(self) -> str:
        return self._url
    
    @property    
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
    
    def is_logout_button_displayed(self) -> bool:

        return super()._is_displayed(self.__log_out_button_locator)