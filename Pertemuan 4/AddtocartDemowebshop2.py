from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/25-virtual-gift-card')

def input_data(self):
    browser.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientName']")
    browser.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientEmail']")
    browser.find_element(By.XPATH, "//input[@id='giftcard_2_SenderName]")
    browser.find_element(By.XPATH, "//input[@id='sgiftcard_2_SenderEmail']")
    browser.find_element(By.XPATH, "//input[@id='giftcard_2_Message']")


def add_tocart2(self):
    #clickk button add to cart
    browser.find_element(By.CLASS_NAME, 'add-to-cart-button-2').click()