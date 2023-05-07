"""
This conftest file contains the driver generation as a fixture that can be used
throughout the project.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


#@pytest.fixture(params=["chrome", "edge"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser") ##-- For selection of browsers
    #browser = request.param # Note this should be 'param' not 'params'. This line is for multiple browser testing.
    print(f"Creating {browser} driver..")
    if browser == "edge":
        my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'edge' but got {browser}")
    yield my_driver
    print(f"Closing {browser} driver..")
    my_driver.quit()

def pytest_addoption(parser):
    """
    Here we added a pytest option to change browsers and automatically fetch the right webdriver
    for it. We then call it with request.config.getoption method on our driver generation.
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (Edge or Chrome)"
    )