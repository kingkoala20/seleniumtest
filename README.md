# Selenium Boilerplate Repo
To be used on Yamaha work later on..

## Resources

[Sample Test Login](https://practicetestautomation.com/practice-test-login/)

[Webdriver Manager Repo](https://github.com/SergeyPirogov/webdriver_manager)

[Selenium Locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)

[Pytest Documentation](https://docs.pytest.org/en/7.1.x/getting-started.html#get-started)

[Selenium Expected Conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html)



## Cheat Sheet

xpath format = `//tag[@attribute='value']`

| Command | Description |
|---|---|
| `driver.get()` | Opens up link in browser |
| `driver.find_element(By.locator, "locator str")` | Returns locator element |
| `driver.current_url` | Returns the current url of the browser |
| `locator.text` | Returns text attr of a locator |
| `locator.click()` | Clicks a locator, mostly used on buttons |
| `locator.send_keys(str)` | Types in the string argument in a locators field |
| `locator.is_displayed()` | Return whether the locator is visible to the user |
| `locator.get_attribute(attr)` | Returns the value of an attribute of a locator |
| `pytest -m <mark>` | Run the marked group of test with the specified name |
| `driver.implicitly_wait(s)` | Implicitly waits s second, same as time.sleep, but within webdriver. Conventionally contained in driver processing |
