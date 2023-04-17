import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome", "edge"])
def driver(request):
    #browser = request.config.getoption("--browser") ##-- For selection of browsers
    browser = request.param # Note this should be 'param' not 'params'. This line is for multiple browser testing.
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
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (Edge or Chrome)"
    )