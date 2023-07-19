import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your ChromeDriver executable
webdriver_service = Service('/Users/apple/Downloads/chromedriver')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the URL
driver.get("https://ecs-qa.kloudship.com")

# Maximize window
driver.maximize_window()

# global wait
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

# Click on the '+' button to add a new package
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//mat-icon[@class='mat-icon notranslate mat-tooltip-trigger material-icons mat-ligature-font mat-icon-no-color']")))

plus_click = driver.find_element(By.XPATH, "//mat-icon[@class='mat-icon notranslate mat-tooltip-trigger material-icons mat-ligature-font mat-icon-no-color']")
plus_click.click()

# Enter package details
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mat-input-5")))

Name = driver.find_element(By.XPATH, "//input[@formcontrolname='name']")
Name.click()
Name.send_keys("Srishti Sharma")

length = driver.find_element(By.XPATH, "//input[@formcontrolname='length']")
length.click()
# Clear the existing text from the input field
length.clear()
length.send_keys("2")


width = driver.find_element(By.XPATH, "//input[@formcontrolname='width']")
width.click()
width.clear()  # Clear the existing text from the input field
width.send_keys("4")

height = driver.find_element(By.CSS_SELECTOR, "[formcontrolname='height']")
height.clear()  # Clear the existing text from the input field
height.send_keys("9")

# Save the package
check = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='check']")
check.click()

# Logout
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//mat-icon[normalize-space()='more_vert']")))

three_dot = driver.find_element(By.XPATH, "//mat-icon[normalize-space()='more_vert']")
three_dot.click()

logout = driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]")
logout.click()

# quit
driver.quit()
