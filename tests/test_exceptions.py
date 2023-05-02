import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXCEPTIONS_URL = "https://practicetestautomation.com/practice-test-exceptions/"
EXCEPTIONS_SAMPLE_ENTRY = "Banana"

class TestExceptions:
    
    
    @pytest.mark.exceptions
    def test_no_such_element(self, driver):
        
        # Opening URL
        driver.get(EXCEPTIONS_URL)
        
        # Clicking Add Button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        
        wait = WebDriverWait (driver, 10)
        row2_field_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))
        
        
        # Verifying Row 2 input field being displayed
        assert row2_field_element.is_displayed(), "Row 2 input should be displayed"
        
        
    @pytest.mark.exceptions
    def test_element_not_interactable(self, driver):
        
        # Open page
        
        driver.get(EXCEPTIONS_URL)
            
        # Click Add Button
        
        add_button_locator = driver.find_element(By.ID, "add_btn").click()
        
        # Wait for the second row to load
        
        wait = WebDriverWait(driver, 10)
        row2_field_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))
        
        # Type text into the second field
        row2_field_element.send_keys(EXCEPTIONS_SAMPLE_ENTRY)
        
        # Click save button
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        
        # Verify text saved
        confirmation_element = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
        
        assert confirmation_element.text == "Row 2 was saved", "Save confirmation text error!"
        
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        
        # Open page
        
        driver.get(EXCEPTIONS_URL)
        
        # Clear input field
        
        driver.find_element(By.ID, "edit_btn").click()
        row1_field_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(row1_field_element))
        row1_field_element.clear()
        
        
        # Type text into the input field
        
        row1_field_element.send_keys('Sushi')
        driver.find_element(By.NAME, "Save").click()
        
        # Verify text changed
        
        confirm = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
        
        assert confirm.text == 'Row 1 was saved', f"Text not changed!. Returned: {confirm.text}"
    
    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        
        # Open page
        
        driver.get(EXCEPTIONS_URL)
        
        # Push add button
        
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        
        # Verify instruction text element is no longer displayed
        
        """
        What happened here is we added an explicit wait for the instruction text to be invisible
        and it returns a bool for invisibility of the element
        """
        
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located((By.XPATH, "//p[@id='instructions']")), "Instruction should not be displayed.")
        
    
    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeoout_exception(self, driver):
        
        # Open page
        
        driver.get(EXCEPTIONS_URL)
        
        # Click add button
        
        driver.find_element(By.XPATH, "//button[@id='add_btn']").click()
        
        # Wait for 3 seconds for the second input field to be displayed
        
        wait = WebDriverWait(driver, 6) # 3 --> 6
        row2_field_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")), "Element is still loading.")
        assert row2_field_element.is_displayed()