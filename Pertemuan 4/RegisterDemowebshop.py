from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/register')

#REGISTER
def success_register(self):
    browser.find_element(By.XPATH, "//input[@id='gender-male']")
    browser.find_element(By.XPATH, "//input[@id='gender-female']")
    browser.find_element(By.XPATH, "//input[@id='FirstName']")
    browser.find_element(By.XPATH, "//input[@id='LastName']")
    browser.find_element(By.XPATH, "//input[@id='Email']")
    browser.find_element(By.XPATH, "//input[@id='Password']")
    browser.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
    browser.find_element(By.XPATH, "//input[@id='register-button']").click()
    get_url = 'https://demowebshop.tricentis.com/'
    self.assertIn('/registerresult/1', get_url)

