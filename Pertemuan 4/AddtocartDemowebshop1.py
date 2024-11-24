from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com')

def add_tochart(self):
    browser.find_element(By.CLASS_NAME, 'product-item')
    #clickk button add to cart
    browser.find_element(By.CLASS_NAME, 'button-2 productpbox-add-to-cart-button').click()
    self.assertIn('/25-virtual-gift-card', browser) 