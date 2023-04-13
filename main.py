## Open Browser

# selenium 4 and google chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)

## Go to webpage
URL = "https://practicetestautomation.com/practice-test-login/"
driver.get(URL)



# 