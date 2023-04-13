# Selenium Boilerplate Repo
To be used on Yamaha work later on..

## Resources

[Sample Test Login](https://practicetestautomation.com/practice-test-login/)

[Webdriver Manager Repo](https://github.com/SergeyPirogov/webdriver_manager)

[Selenium Locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)



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
