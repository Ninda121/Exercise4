from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/login')

def succes_login(self):
    browser.find_element(By.XPATH, "//input[@id='Email']")
    browser.find_element(By.XPATH, "//input[@id='Password']")
    browser.find_element(By.XPATH, "//input[@id='register-button']").click()
    get_url = 'https://demowebshop.tricentis.com/'
    self.assertIn(get_url)

def failed_login(self):
    browser.find_element(By.XPATH, "//input[@id='Email']")
    browser.find_element(By.XPATH, "//input[@id='Password']")
    browser.find_element(By.XPATH, "//input[@id='register-button']").click()
    error_message = browser.find_element(By.CLASS_NAME, 'massage-error').text
    self.assertIn("Login was unsuccessful. Please correct the errors and try again.The credentials provided are incorrect", error_message)