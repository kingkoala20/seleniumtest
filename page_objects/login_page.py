from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage 

class LoginPage(BasePage):
    
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_btn_locator = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.ID, "error")
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._driver = driver
        
        
    def open(self):
        super()._open_url(self.__url)
        

    def execute_login(self, user: str, pw: str):
        super()._type(self.__username_field, user)
        super()._type(self.__password_field, pw)
        super()._click(self.__submit_btn_locator)
        
    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time = 3)