from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_logout():
    # Set up Firefox WebDriver
    driver = webdriver.Firefox(executable_path="C:\\Users\\centr\\OneDrive\\Documents\\login\\geckodriver.exe")

    # Replace 'http://example.com' with the URL of your login page
    url = 'https://lms.careertiq.com/'
    driver.get(url)

    def login():
        # Find login button and click
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tl-cms-nav-login'))
        )
        login_button.click()

        # Wait for username field to be visible
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'tl-shared-username'))
        )

        # Read username and password from cred.txt
        with open('cred.txt', 'r') as file:
            credentials = file.read().splitlines()
            username = credentials[0]
            password = credentials[1]

        # Enter username and password
        username_field.send_keys(username)
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password)

        # Click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][name="submit"][value="Login"]'))
        )
        login_button.click()

        # Wait for 5 seconds
        time.sleep(5)

        # Perform logout
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tl-navbar-logout-icon'))
        )
        logout_button.click()

    # Perform login and logout
    login()

    # Close the browser
    driver.quit()

    # Sleep for 1 hour and 2 minutes after logout
    time.sleep((60 * 60) + (2 * 60))
    #time.sleep(2)
# Run the login and logout process in a loop
while True:
    login_and_logout()
