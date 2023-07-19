# Set the path to your ChromeDriver executable
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webdriver_service = Service('/Users/apple/Downloads/chromedriver')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the URL
driver.get("https://ecs-qa.kloudship.com")

# Maximize window
driver.maximize_window()
driver.implicitly_wait(5)


# Find the email input field and enter the email
email_input = driver.find_element(By.ID, "mat-input-0")
email_input.send_keys("kloudship.qa.automation@mailinator.com")

# Find the password input field and enter the password
password_input = driver.find_element(By.ID, "password-field")
password_input.send_keys("Password1")

# Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Wait for the next page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Packages']")))

# Click on Packages
package = driver.find_element(By.XPATH, "//span[normalize-space()='Packages']")
package.click()

try:
    elem = driver.find_element(By.XPATH, "//div[@class='padding list-text']")
    driver.implicitly_wait(5)
    actions = ActionChains(driver)
    actions.move_to_element(elem).perform()
except NoSuchElementException:
    print("Element not found. Handle the exception here.")
    # Take a screenshot
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = f"/Users/apple/PycharmProjects/Impledge/ImpledgeTest/ErrorScreenshots/NoPackage_screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved as {screenshot_file}")
    exit()

# elem = driver.find_element(By.XPATH, "//div[@class= 'padding list-text']")
# time.sleep(4)
# actions = ActionChains(driver)
# actions.move_to_element(elem).perform()

delete_element = driver.find_element(By.XPATH, "//div[@dialogicon='delete']")
delete_element.click()

buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    if button.text == "Delete Package Type":
        driver.implicitly_wait(5)
        button.click()
        break

# Wait for the <simple-snack-bar> element to be visible
snackbar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "simple-snack-bar")))

# Get the text of the snackbar message
snackbar_text = snackbar.find_element(By.CLASS_NAME, "mat-simple-snack-bar-content").text

# Extract the dynamic name from the success message
dynamic_name = snackbar_text.split(" has been successfully deleted")[0]

# Verify the success message using an assertion or other validation logic
assert "successfully deleted" in snackbar_text, f"Deletion failed for {dynamic_name}"

ok_button = snackbar.find_element(By.CSS_SELECTOR, "button.mat-button")
ok_button.click()

# quit
driver.quit()
